import os
import yaml
import json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES_DIR = os.path.join(REPO_ROOT, 'sources')
OUTPUT_FILE = os.path.join(REPO_ROOT, 'index.html')
GITHUB_BASE_URL = "https://github.com/bitcoreos/skills.md/blob/main/"

def parse_skill_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return None
            
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None
            
        frontmatter = yaml.safe_load(parts[1])
        if not isinstance(frontmatter, dict):
            return None
            
        # Add relative path for linking
        rel_path = os.path.relpath(filepath, REPO_ROOT)
        frontmatter['file_path'] = rel_path
        return frontmatter
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def scan_skills():
    skills = []
    for root, dirs, files in os.walk(SOURCES_DIR):
        for file in files:
            if file == 'SKILL.md':
                filepath = os.path.join(root, file)
                skill_data = parse_skill_file(filepath)
                if skill_data:
                    skills.append(skill_data)
    return skills

def generate_html(skills):
    # Sort skills by name
    skills.sort(key=lambda x: x.get('name', 'Untitled'))
    
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BITcore Skill Index</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #38bdf8;
            --border: #334155;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 2rem;
            line-height: 1.5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        header {
            margin-bottom: 2rem;
            text-align: center;
        }
        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(to right, var(--accent), #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        #search {
            width: 100%;
            max-width: 600px;
            padding: 1rem;
            font-size: 1.1rem;
            border-radius: 0.5rem;
            border: 1px solid var(--border);
            background-color: var(--card-bg);
            color: var(--text-main);
            margin-bottom: 2rem;
        }
        #search:focus {
            outline: 2px solid var(--accent);
            border-color: transparent;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }
        .skill-card {
            background-color: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 0.75rem;
            padding: 1.5rem;
            transition: transform 0.2s, border-color 0.2s;
            display: flex;
            flex-direction: column;
        }
        .skill-card:hover {
            transform: translateY(-2px);
            border-color: var(--accent);
        }
        .skill-name {
            font-size: 1.25rem;
            font-weight: 600;
            margin: 0 0 0.5rem 0;
            color: var(--accent);
        }
        .skill-desc {
            color: var(--text-muted);
            font-size: 0.95rem;
            flex-grow: 1;
            margin-bottom: 1rem;
        }
        .skill-meta {
            font-size: 0.8rem;
            color: #64748b;
            margin-top: auto;
            padding-top: 1rem;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        a.source-link {
            color: var(--accent);
            text-decoration: none;
            font-weight: 500;
        }
        a.source-link:hover {
            text-decoration: underline;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>BITcore Skill Index</h1>
            <input type="text" id="search" placeholder="Search skills by name or description...">
            <div id="count" style="color: var(--text-muted);"></div>
        </header>
        <div id="skill-grid" class="grid">
            <!-- Skills will be injected here -->
            {% for skill in skills %}
            <div class="skill-card" data-name="{{ skill.get('name', '') | lower }}" data-desc="{{ skill.get('description', '') | lower }}">
                <h2 class="skill-name">{{ skill.get('name', 'Untitled') }}</h2>
                <p class="skill-desc">{{ skill.get('description', 'No description provided.') }}</p>
                <div class="skill-meta">
                    <span>v{{ skill.get('version', '1.0.0') }}</span>
                    <a href="{{ github_base }}{{ skill.get('file_path', '') }}" target="_blank" class="source-link">View Source &rarr;</a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <script>
        const searchInput = document.getElementById('search');
        const cards = document.querySelectorAll('.skill-card');
        const countDisplay = document.getElementById('count');

        function updateCount() {
            const visible = document.querySelectorAll('.skill-card:not(.hidden)').length;
            countDisplay.textContent = `Showing ${visible} skills`;
        }

        searchInput.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            cards.forEach(card => {
                const name = card.getAttribute('data-name');
                const desc = card.getAttribute('data-desc');
                if (name.includes(term) || desc.includes(term)) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
            updateCount();
        });
        
        // Init count
        updateCount();
    </script>
</body>
</html>
    """
    
    # Simple template rendering
    rendered = html_template.replace('{{ github_base }}', GITHUB_BASE_URL)
    
    # We need to construct the loop content manually since we don't have jinja2
    cards_html = []
    for skill in skills:
        name = skill.get('name', 'Untitled')
        desc = skill.get('description', 'No description provided.')
        version = skill.get('version', '1.0.0')
        file_path = skill.get('file_path', '')
        
        # Escape HTML special chars roughly
        name_safe = str(name).replace('<', '&lt;').replace('>', '&gt;')
        desc_safe = str(desc).replace('<', '&lt;').replace('>', '&gt;')
        
        card = f"""
            <div class="skill-card" data-name="{name_safe.lower()}" data-desc="{desc_safe.lower()}">
                <h2 class="skill-name">{name_safe}</h2>
                <p class="skill-desc">{desc_safe}</p>
                <div class="skill-meta">
                    <span>v{version}</span>
                    <a href="{GITHUB_BASE_URL}{file_path}" target="_blank" class="source-link">View Source &rarr;</a>
                </div>
            </div>"""
        cards_html.append(card)
    
    # Replace the jinja-like block with actual content
    start_marker = "{% for skill in skills %}"
    end_marker = "{% endfor %}"
    
    start_idx = rendered.find(start_marker)
    end_idx = rendered.find(end_marker) + len(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        final_html = rendered[:start_idx] + "\n".join(cards_html) + rendered[end_idx:]
    else:
        final_html = rendered
    
    return final_html

def main():
    print("Scanning for skills...")
    skills = scan_skills()
    print(f"Found {len(skills)} skills.")
    
    print("Generating HTML...")
    html_content = generate_html(skills)
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Site generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
