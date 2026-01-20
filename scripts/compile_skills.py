import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(REPO_DIR, "sources")
OUTPUT_DIR = os.path.join(REPO_DIR, "compiled")

LANGUAGE_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".json": "json",
    ".md": "markdown",
    ".markdown": "markdown",
    ".txt": "text",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".sh": "bash",
    ".ps1": "powershell",
    ".css": "css",
    ".html": "html",
}

PROVIDER_MARKERS = {
    "openai": "/openai/skills/",
    "anthropic": "/anthropic/skills/",
    "vercel": "/vercel/skills/",
    "agentskills": "/agentskills/skills-ref/",
}


def parse_frontmatter(content):
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, content
    fm_lines = []
    i = 1
    while i < len(lines):
        if lines[i].strip() == "---":
            i += 1
            break
        fm_lines.append(lines[i])
        i += 1
    body = "\n".join(lines[i:]) if i < len(lines) else ""
    data = {}
    current_key = None
    in_block = False
    for line in fm_lines:
        if not line.strip():
            continue
        if in_block and (line.startswith(" ") or line.startswith("\t")):
            data[current_key] += "\n" + line.strip()
            continue
        match = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            if value in ("|", ">"):
                data[key] = ""
                current_key = key
                in_block = True
            else:
                data[key] = value
                current_key = key
                in_block = False
    return data, body


def normalize_origin(origin):
    return origin.replace("\\", "/") if origin else ""


def extract_origin_dir(origin):
    normalized = normalize_origin(origin)
    if not normalized or normalized == "Unknown":
        return None
    return os.path.dirname(normalized)


def origin_to_relpath(origin, provider):
    normalized = normalize_origin(origin)
    if not normalized or normalized == "Unknown":
        return None
    marker = f"/{provider}/"
    if marker not in normalized:
        return None
    tail = normalized.split(marker, 1)[1].lstrip("/")
    base, _ext = os.path.splitext(tail)
    return base.strip("/")


def find_skill_files():
    entries = []
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.upper() != "SKILL.MD":
                continue
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, REPO_DIR)
            with open(path, "r", encoding="utf-8", errors="ignore") as handle:
                content = handle.read()
            frontmatter, body = parse_frontmatter(content)
            parts = rel_path.split(os.sep)
            provider = parts[1] if len(parts) > 1 else "Unknown"
            origin = frontmatter.get("origin") or frontmatter.get("source") or "Unknown"
            entries.append(
                {
                    "path": path,
                    "rel_path": rel_path,
                    "provider": provider,
                    "origin": origin,
                    "frontmatter": frontmatter,
                    "body": body.strip(),
                }
            )
    return entries


def is_markdown_source(origin):
    if not origin or origin == "Unknown":
        return False
    ext = os.path.splitext(origin)[1].lower()
    return ext in (".md", ".markdown")


def render_frontmatter(frontmatter):
    if not frontmatter:
        return ""
    lines = ["---"]
    for key, value in frontmatter.items():
        lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def render_attachment(entry):
    origin = entry["origin"]
    filename = os.path.basename(origin) if origin not in ("", "Unknown") else "attachment"
    ext = os.path.splitext(filename)[1].lower()
    language = LANGUAGE_MAP.get(ext, "")
    header = f"### {filename}\n\n"
    source_line = f"Source: `{origin}`\n\n" if origin and origin != "Unknown" else ""
    fenced = f"```{language}\n{entry['body']}\n```\n"
    return header + source_line + fenced


def compile_skills():
    entries = find_skill_files()
    md_entries = []
    attachments_by_dir = {}
    md_by_dir = {}

    for entry in entries:
        origin = entry["origin"]
        origin_dir = extract_origin_dir(origin)
        if not origin_dir:
            continue
        entry["origin_dir"] = origin_dir
        if is_markdown_source(origin):
            md_entries.append(entry)
            md_by_dir.setdefault(origin_dir, []).append(entry)
        else:
            attachments_by_dir.setdefault(origin_dir, []).append(entry)

    if os.path.exists(OUTPUT_DIR):
        for root, dirs, files in os.walk(OUTPUT_DIR, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
    else:
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    written = 0
    def choose_primary_md(candidates):
        if len(candidates) == 1:
            return candidates[0]
        for entry in candidates:
            basename = os.path.basename(entry["origin"]).lower()
            if basename in ("skill.md", "readme.md"):
                return entry
        return None

    for entry in sorted(md_entries, key=lambda e: e["origin"]):
        provider = entry["provider"]
        origin_dir = entry["origin_dir"]
        candidates = md_by_dir.get(origin_dir, [])
        primary = choose_primary_md(candidates)
        rel_path = origin_to_relpath(entry["origin"], provider)
        if not rel_path:
            continue
        out_dir = os.path.join(OUTPUT_DIR, provider, rel_path.replace("/", os.sep))
        os.makedirs(out_dir, exist_ok=True)
        frontmatter_data = dict(entry["frontmatter"])
        if "registry_path" not in frontmatter_data:
            frontmatter_data["registry_path"] = entry["rel_path"]
        frontmatter = render_frontmatter(frontmatter_data)
        content = entry["body"].strip()
        attachments = sorted(attachments_by_dir.get(origin_dir, []), key=lambda e: e["origin"])
        if attachments and (primary is None or primary is entry):
            content += "\n\n## Bundled Sources\n\n"
            for attachment in attachments:
                content += render_attachment(attachment) + "\n"
        compiled = "\n\n".join([part for part in [frontmatter, content] if part])
        out_path = os.path.join(out_dir, "SKILL.md")
        with open(out_path, "w", encoding="utf-8") as handle:
            handle.write(compiled.strip() + "\n")
        written += 1
    return written


if __name__ == "__main__":
    count = compile_skills()
    print(f"Compiled {count} skills into {OUTPUT_DIR}")
