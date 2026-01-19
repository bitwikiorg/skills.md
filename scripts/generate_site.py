import os
import re

# Configuration
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_FILE = os.path.join(REPO_DIR, 'skills.md')
OUTPUT_FILE = os.path.join(REPO_DIR, 'index.html')

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BitcoreOS Skills Registry</title>
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
            max_width: 1200px;
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
        }
        .skill-title {
            font-weight: 600;
            font-size: 1.1rem;
            color: var(--accent-blue);
            font-family: var(--font-mono);
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
        .source-link {
            color: var(--text-muted);
            text-decoration: none;
            transition: color 0.2s;
        }
        .source-link:hover {
            color: var(--accent-blue);
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
        <h1>BitcoreOS // Skills Registry</h1>
        <div class="search-container">
            <input type="text" id="search-input" placeholder="Filter skills by name or description..." autofocus>
        </div>
    </header>
    <main class="grid" id="skills-grid">
        __SKILLS_CONTENT__
    </main>
    <div id="toast" class="toast">Copied to clipboard!</div>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const searchInput = document.getElementById('search-input');
            const cards = document.querySelectorAll('.card');
            searchInput.addEventListener('input', (e) => {
                const term = e.target.value.toLowerCase();
                cards.forEach(card => {
                    const title = card.dataset.title.toLowerCase();
                    const desc = card.dataset.desc.toLowerCase();
                    if (title.includes(term) || desc.includes(term)) {
                        card.classList.remove('hidden');
                    } else {
                        card.classList.add('hidden');
                    }
                });
            });
        });
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => { showToast(); });
        }
        function showToast() {
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => { toast.classList.remove('show'); }, 2000);
        }
    </script>
</body>
</html>"""

def parse_skills(file_path):
    skills = []
    if not os.path.exists(file_path):
        return skills
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by H2 headers
    sections = re.split(r'^##\s+', content, flags=re.MULTILINE)
    for section in sections:
        if not section.strip(): continue
        lines = section.strip().splitlines()
        title = lines[0].strip()
        body_lines = []
        provider = "Unknown"
        for line in lines[1:]:
            if line.strip().startswith('- Provider:') or line.strip().startswith('* Provider:'):
                provider = line.split(':', 1)[1].strip()
            else:
                body_lines.append(line)
        description = '\n'.join(body_lines).strip() or "No description provided."
        skills.append({'title': title, 'description': description, 'provider': provider})
    return skills

def generate_html(skills):
    skills_html = ""
    for skill in skills:
        safe_title = skill['title'].replace('"', '&quot;')
        safe_desc = skill['description'].replace('"', '&quot;')
        card = f"""
        <article class="card" data-title="{safe_title}" data-desc="{safe_desc}">
            <div class="card-header">
                <div class="skill-title">{skill['title']}</div>
                <button class="copy-btn" onclick="copyToClipboard('{safe_title}')" title="Copy Skill Name">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                </button>
            </div>
            <div class="card-body">{skill['description']}</div>
            <div class="card-footer">
                <span class="badge">{skill['provider']}</span>
                <a href="skills.md" class="source-link">View Source</a>
            </div>
        </article>
        """
        skills_html += card
    return HTML_TEMPLATE.replace('__SKILLS_CONTENT__', skills_html)

if __name__ == "__main__":
    skills = parse_skills(SKILLS_FILE)
    html = generate_html(skills)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
