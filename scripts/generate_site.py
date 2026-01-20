import os
import re
import html

# Configuration
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FILE = os.path.join(REPO_DIR, 'index.html')
SOURCES_DIR = os.path.join(REPO_DIR, 'sources')

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skills Registry</title>
    <style>
        :root {
            --bg-color: #0d1117;
            --card-bg: #161b22;
            --text-main: #c9d1d9;
            --text-muted: #8b949e;
            --accent-green: #238636;
            --accent-blue: #58a6ff;
            --border-color: #30363d;
            --font-mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.5;
            padding: 2rem;
        }
        header {
            max-width: 1200px;
            margin: 0 auto 2rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }
        h1 {
            font-family: var(--font-mono);
            font-size: 1.5rem;
            color: var(--text-main);
        }
        .meta-bar {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
            font-size: 0.85rem;
            color: var(--text-muted);
            max-width: 1200px;
            margin: 0 auto 1.5rem;
        }
        .refs {
            max-width: 1200px;
            margin: 0 auto 2rem;
            padding: 1rem;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background-color: rgba(13, 17, 23, 0.6);
        }
        .refs h2 {
            font-size: 1rem;
            margin-bottom: 0.75rem;
            font-family: var(--font-mono);
        }
        .refs ul {
            list-style: none;
            display: grid;
            gap: 0.4rem;
        }
        .refs a {
            color: var(--accent-blue);
            text-decoration: none;
        }
        .refs a:hover {
            text-decoration: underline;
        }
        .banner {
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 0.5rem 0.75rem;
            background-color: rgba(56, 139, 253, 0.08);
        }
        .banner a {
            color: var(--accent-blue);
            text-decoration: none;
        }
        .banner a:hover {
            text-decoration: underline;
        }
        .search-container { flex-grow: 1; max-width: 400px; }
        #search-input {
            width: 100%;
            padding: 0.5rem 1rem;
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            color: var(--text-main);
            font-family: var(--font-mono);
            font-size: 0.9rem;
        }
        #search-input:focus {
            outline: none;
            border-color: var(--accent-blue);
            box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.3);
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        .card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            transition: transform 0.2s, border-color 0.2s;
        }
        .card:hover {
            border-color: var(--accent-blue);
            transform: translateY(-2px);
        }
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1rem;
            gap: 0.75rem;
        }
        .skill-title {
            font-weight: 600;
            font-size: 1.1rem;
            color: var(--accent-blue);
            font-family: var(--font-mono);
            word-break: break-word;
        }
        .copy-btn {
            background: none;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            padding: 4px;
            border-radius: 4px;
            transition: color 0.2s, background-color 0.2s;
        }
        .copy-btn:hover {
            color: var(--text-main);
            background-color: var(--border-color);
        }
        .card-body {
            flex-grow: 1;
            font-size: 0.95rem;
            color: var(--text-main);
            margin-bottom: 1.5rem;
            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: 4;
            -webkit-box-orient: vertical;
        }
        .card-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid var(--border-color);
            padding-top: 1rem;
            font-size: 0.85rem;
        }
        .badge {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            background-color: rgba(56, 139, 253, 0.15);
            color: var(--accent-blue);
            border: 1px solid rgba(56, 139, 253, 0.4);
            font-family: var(--font-mono);
            font-size: 0.75rem;
        }
        .badge.muted {
            background-color: rgba(139, 148, 158, 0.15);
            color: var(--text-muted);
            border-color: rgba(139, 148, 158, 0.4);
        }
        .pill {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            background-color: rgba(35, 134, 54, 0.15);
            color: var(--accent-green);
            border: 1px solid rgba(35, 134, 54, 0.4);
            font-family: var(--font-mono);
            font-size: 0.75rem;
        }
        .info-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 0.75rem;
            font-size: 0.8rem;
            color: var(--text-muted);
        }
        .skill-content {
            background-color: rgba(22, 27, 34, 0.6);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 0.75rem;
            font-family: var(--font-mono);
            font-size: 0.78rem;
            white-space: pre-wrap;
            max-height: 260px;
            overflow: auto;
        }
        details summary {
            cursor: pointer;
            color: var(--accent-blue);
            font-family: var(--font-mono);
        }
        details summary:hover {
            text-decoration: underline;
        }
        .source-link {
            color: var(--text-muted);
            text-decoration: none;
            transition: color 0.2s;
        }
        .source-link:hover {
            color: var(--accent-blue);
            text-decoration: underline;
        }
        .link-group {
            display: flex;
            gap: 0.75rem;
            align-items: center;
            flex-wrap: wrap;
        }
        .link-group a {
            color: var(--accent-blue);
            text-decoration: none;
            font-size: 0.85rem;
        }
        .link-group a:hover {
            text-decoration: underline;
        }
        .hidden { display: none !important; }
        .toast {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: var(--accent-green);
            color: white;
            padding: 10px 20px;
            border-radius: 6px;
            opacity: 0;
            transition: opacity 0.3s;
            pointer-events: none;
            font-family: var(--font-mono);
        }
        .toast.show { opacity: 1; }
    </style>
</head>
<body>
    <header>
        <h1>Skills Registry</h1>
        <div class="search-container">
            <input type="text" id="search-input" placeholder="Filter skills by name, content, provider, license, or source..." autofocus>
        </div>
    </header>
    <div class="meta-bar">
        <div id="registry-banner" class="banner"></div>
        <div id="skills-count"></div>
    </div>
    <section class="refs">
        <h2>Official References</h2>
        <ul>
            <li><a href="https://code.claude.com/docs/en/skills" target="_blank" rel="noopener">https://code.claude.com/docs/en/skills</a></li>
            <li><a href="https://github.com/anthropics/skills" target="_blank" rel="noopener">https://github.com/anthropics/skills</a></li>
            <li><a href="https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview" target="_blank" rel="noopener">https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview</a></li>
            <li><a href="https://agentskills.io/home" target="_blank" rel="noopener">https://agentskills.io/home</a></li>
            <li><a href="https://github.com/agentskills/agentskills/tree/main/skills-ref" target="_blank" rel="noopener">https://github.com/agentskills/agentskills/tree/main/skills-ref</a></li>
            <li><a href="https://github.com/openai/skills" target="_blank" rel="noopener">https://github.com/openai/skills</a></li>
            <li><a href="https://github.com/vercel-labs/agent-skills" target="_blank" rel="noopener">https://github.com/vercel-labs/agent-skills</a></li>
            <li><a href="https://github.com/langchain-ai/deepagents/tree/f878123eebf245dc609dea49a6a95714153f9b65/libs/deepagents-cli/examples/skills" target="_blank" rel="noopener">https://github.com/langchain-ai/deepagents/tree/f878123eebf245dc609dea49a6a95714153f9b65/libs/deepagents-cli/examples/skills</a></li>
            <li><a href="https://github.com/langchain-ai/deepagents/tree/f878123eebf245dc609dea49a6a95714153f9b65/examples/content-builder-agent/skills" target="_blank" rel="noopener">https://github.com/langchain-ai/deepagents/tree/f878123eebf245dc609dea49a6a95714153f9b65/examples/content-builder-agent/skills</a></li>
        </ul>
    </section>
    <main class="grid" id="skills-grid">
        __SKILLS_CONTENT__
    </main>
    <div id="toast" class="toast">Copied to clipboard!</div>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const searchInput = document.getElementById('search-input');
            const cards = document.querySelectorAll('.card');
            const count = document.getElementById('skills-count');
            count.textContent = `${cards.length} skills indexed`;
            searchInput.addEventListener('input', (e) => {
                const term = e.target.value.toLowerCase();
                cards.forEach(card => {
                    const content = card.querySelector('.skill-content');
                    const haystack = (card.dataset.search + ' ' + (content ? content.textContent : '')).toLowerCase();
                    if (haystack.includes(term)) {
                        card.classList.remove('hidden');
                    } else {
                        card.classList.add('hidden');
                    }
                });
            });
            const banner = document.getElementById('registry-banner');
            const host = window.location.host;
            if (host.includes('bitcoreos.github.io')) {
                banner.innerHTML = 'Dev registry: bitcoreos/skills.md. Public registry: <a href="https://bitwikiorg.github.io/skills.md/">bitwikiorg.github.io/skills.md</a>';
            } else if (host.includes('bitwikiorg.github.io')) {
                banner.innerHTML = 'Public registry: bitwikiorg/skills.md. Dev registry: <a href="https://bitcoreos.github.io/skills.md/">bitcoreos.github.io/skills.md</a>';
            } else {
                banner.textContent = 'Skills registry mirror';
            }
        });
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => { showToast(); });
        }
        function copySkill(button) {
            const card = button.closest('.card');
            const content = card.querySelector('.skill-content');
            if (content) {
                navigator.clipboard.writeText(content.textContent).then(() => { showToast(); });
            }
        }
        function hydrateLinks() {
            const host = window.location.host;
            let repoBase = 'https://github.com/bitcoreos/skills.md';
            if (host.includes('bitwikiorg.github.io')) {
                repoBase = 'https://github.com/bitwikiorg/skills.md';
            }
            document.querySelectorAll('[data-path]').forEach(link => {
                const path = link.getAttribute('data-path');
                link.setAttribute('href', `${repoBase}/blob/main/${path}`);
            });
        }
        document.addEventListener('DOMContentLoaded', hydrateLinks);
        function showToast() {
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => { toast.classList.remove('show'); }, 2000);
        }
    </script>
</body>
</html>"""

def parse_frontmatter(content):
    lines = content.splitlines()
    if not lines or lines[0].strip() != '---':
        return {}, content
    fm_lines = []
    i = 1
    while i < len(lines):
        if lines[i].strip() == '---':
            i += 1
            break
        fm_lines.append(lines[i])
        i += 1
    body = '\n'.join(lines[i:]) if i < len(lines) else ''
    data = {}
    current_key = None
    in_block = False
    for line in fm_lines:
        if not line.strip():
            continue
        if in_block and (line.startswith(' ') or line.startswith('\t')):
            data[current_key] += '\n' + line.strip()
            continue
        match = re.match(r'^([A-Za-z0-9_-]+)\s*:\s*(.*)$', line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            if value in ('|', '>'):
                data[key] = ''
                current_key = key
                in_block = True
            else:
                data[key] = value
                current_key = key
                in_block = False
    return data, body

PROVIDER_INFO = {
    "openai": {
        "repo": "https://github.com/openai/skills",
        "license_mode": "per-skill",
        "license_label": "LICENSE.txt",
    },
    "anthropic": {
        "repo": "https://github.com/anthropics/skills",
        "license_mode": "per-skill",
        "license_label": "LICENSE.txt",
    },
    "vercel": {
        "repo": "https://github.com/vercel-labs/agent-skills",
        "license_url": "https://github.com/vercel-labs/agent-skills",
        "license_label": "See repository",
    },
    "agentskills": {
        "repo": "https://github.com/agentskills/agentskills",
        "license_url": "https://github.com/agentskills/agentskills/blob/main/skills-ref/LICENSE",
        "license_label": "skills-ref/LICENSE",
    },
    "langchain": {
        "repo": "https://github.com/langchain-ai/deepagents",
        "license_url": "https://github.com/langchain-ai/deepagents/blob/main/LICENSE",
        "license_label": "LICENSE",
    },
    "bithub": {
        "repo": "https://github.com/bitwikiorg/skills.md",
        "license_url": "https://github.com/bitwikiorg/skills.md",
        "license_label": "See repository",
    },
}

def extract_upstream_path(origin, marker, base_url):
    if not origin or marker not in origin:
        return None
    tail = origin.split(marker, 1)[1].lstrip('/')
    return f"{base_url}/{tail}"

def derive_license_url(origin, provider):
    info = PROVIDER_INFO.get(provider, {})
    if info.get("license_mode") != "per-skill":
        return info.get("license_url")
    if provider == "openai" and "/openai/skills/" in origin:
        tail = origin.split("/openai/skills/", 1)[1].lstrip("/")
        parts = tail.split("/")
        if len(parts) >= 2 and parts[0].startswith("."):
            skill_dir = f"{parts[0]}/{parts[1]}"
        else:
            skill_dir = parts[0] if parts else ""
        if skill_dir:
            return f"https://github.com/openai/skills/blob/main/skills/{skill_dir}/LICENSE.txt"
    if provider == "anthropic" and "/anthropic/skills/" in origin:
        tail = origin.split("/anthropic/skills/", 1)[1].lstrip("/")
        parts = tail.split("/")
        skill_dir = parts[0] if parts else ""
        if skill_dir:
            return f"https://github.com/anthropics/skills/blob/main/skills/{skill_dir}/LICENSE.txt"
    return info.get("license_url")

def derive_upstream_url(origin, provider):
    if not origin:
        return None
    if origin.startswith("http://") or origin.startswith("https://"):
        return origin
    if "/openai/skills/" in origin:
        return extract_upstream_path(origin, "/openai/skills/", "https://github.com/openai/skills/blob/main/skills")
    if "/anthropic/skills/" in origin:
        return extract_upstream_path(origin, "/anthropic/skills/", "https://github.com/anthropics/skills/blob/main/skills")
    if "/agentskills/skills-ref/" in origin:
        return extract_upstream_path(origin, "/agentskills/skills-ref/", "https://github.com/agentskills/agentskills/blob/main/skills-ref")
    if "/deepagents/" in origin:
        return extract_upstream_path(origin, "/deepagents/", "https://github.com/langchain-ai/deepagents/blob/main")
    return None

def extract_snippet(text):
    cleaned = []
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        if line.strip().startswith('#'):
            continue
        cleaned.append(line)
    snippet = ' '.join(' '.join(cleaned).split())
    return snippet[:280] + ('...' if len(snippet) > 280 else '')

def collect_skills():
    skills = []
    for root, _, files in os.walk(SOURCES_DIR):
        for file in files:
            if not (file.endswith('.js') or file.upper() == 'SKILL.MD'):
                continue
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, REPO_DIR)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            frontmatter, body = parse_frontmatter(content)
            parts = rel_path.split(os.sep)
            provider = parts[1] if len(parts) > 1 else "Unknown"
            skill_id = frontmatter.get('id') or frontmatter.get('name') or os.path.splitext(file)[0]
            description = frontmatter.get('description') or extract_snippet(body) or "No description provided."
            origin = frontmatter.get('origin') or frontmatter.get('source') or "Unknown"
            version = frontmatter.get('version') or "Unknown"
            license_id = frontmatter.get('spdx-id') or frontmatter.get('spdx_id') or frontmatter.get('license') or "Unknown"
            skill_type = 'SKILL.md' if file.upper() == 'SKILL.MD' else 'js'
            upstream_url = derive_upstream_url(origin, provider)
            license_url = None
            license_label = None
            if license_id != "Unknown":
                license_label = license_id
                if re.match(r"^[A-Za-z0-9\.\-+]+$", license_id):
                    license_url = f"https://spdx.org/licenses/{license_id}.html"
            if not license_label:
                license_url = derive_license_url(origin, provider)
                provider_info = PROVIDER_INFO.get(provider, {})
                license_label = provider_info.get("license_label", "See source")
            search_blob = " ".join([
                skill_id,
                description,
                provider,
                origin,
                version,
                license_label,
                rel_path,
                skill_type,
            ])
            skills.append({
                'id': skill_id,
                'description': description,
                'provider': provider,
                'origin': origin,
                'upstream_url': upstream_url or "",
                'version': version,
                'license': license_label,
                'license_url': license_url or "",
                'path': rel_path,
                'type': skill_type,
                'content': body.strip() or "No content available.",
                'search': search_blob,
            })
    skills.sort(key=lambda s: (s['provider'].lower(), s['id'].lower()))
    return skills

def generate_html(skills):
    skills_html = ""
    for skill in skills:
        display_id = html.escape(str(skill['id']), quote=True)
        safe_desc = html.escape(str(skill['description']), quote=True)
        safe_path = html.escape(str(skill['path']), quote=True)
        safe_search = html.escape(re.sub(r'\s+', ' ', str(skill['search'])), quote=True)
        safe_content = html.escape(str(skill['content']), quote=True)
        id_js = str(skill['id']).replace('\\', '\\\\').replace("'", "\\'")
        upstream_url = html.escape(str(skill['upstream_url']), quote=True)
        license_url = html.escape(str(skill['license_url']), quote=True)
        provider_info = PROVIDER_INFO.get(skill['provider'], {})
        provider_repo = html.escape(str(provider_info.get('repo', '')), quote=True)
        card = f"""
        <article class="card" data-search="{safe_search}">
            <div class="card-header">
                <div class="skill-title">{display_id}</div>
                <button class="copy-btn" onclick="copyToClipboard('{id_js}')" title="Copy Skill ID">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                </button>
            </div>
            <div class="info-row">
                <span class="badge">{html.escape(str(skill['provider']))}</span>
                <span class="pill">{html.escape(str(skill['type']))}</span>
                <span class="badge muted">License: {html.escape(str(skill['license']))}</span>
                <span class="badge muted">Version: {html.escape(str(skill['version']))}</span>
            </div>
            <div class="card-body">{safe_desc}</div>
            <details>
                <summary>View skill</summary>
                <pre class="skill-content">{safe_content}</pre>
            </details>
            <div class="card-footer">
                <div class="link-group">
                    <a data-path="{safe_path}" class="source-link">Registry File</a>
                    {f'<a href="{upstream_url}" class="source-link" target="_blank" rel="noopener">Upstream File</a>' if upstream_url else ''}
                    {f'<a href="{provider_repo}" class="source-link" target="_blank" rel="noopener">Provider Repo</a>' if (not upstream_url and provider_repo) else ''}
                    {f'<a href="{license_url}" class="source-link" target="_blank" rel="noopener">License: {html.escape(str(skill["license"]), quote=True)}</a>' if license_url else f'<span class="badge muted">License: {html.escape(str(skill["license"]), quote=True)}</span>'}
                    <button class="copy-btn" onclick="copySkill(this)" title="Copy Skill Content">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    </button>
                </div>
            </div>
        </article>
        """
        skills_html += card
    return HTML_TEMPLATE.replace('__SKILLS_CONTENT__', skills_html)

if __name__ == "__main__":
    skills = collect_skills()
    html = generate_html(skills)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
