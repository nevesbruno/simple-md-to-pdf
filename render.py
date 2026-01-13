import sys
from pathlib import Path
from markdown import markdown
from weasyprint import HTML

CSS_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --font-base: 12.8px;
    --color-bg: #ffffff;
    --color-text: #1a1a2e;
    --color-muted: #4a4a68;
    --color-border: #d0d0e0;
    --color-code-bg: #1e1e2e;
    --color-code-text: #cdd6f4;
    --color-table-header: #f0f0f5;
    --color-table-alt: #f8f8fc;
}

* { box-sizing: border-box; }

body {
    font-family: 'Poppins', sans-serif;
    font-size: var(--font-base);
    line-height: 1.6;
    color: var(--color-text);
    background: var(--color-bg);
    margin: 0;
    padding: 40px;
}

h1, h2, h3, h4, h5, h6 {
    font-weight: 700;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    line-height: 1.3;
}

h1 { font-size: 1.8em; border-bottom: 2px solid var(--color-border); padding-bottom: 0.3em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.25em; }
h4 { font-size: 1.1em; }

p { margin: 0.8em 0; }

/* Code blocks */
pre {
    background: var(--color-code-bg);
    color: var(--color-code-text);
    border-radius: 6px;
    padding: 16px 20px;
    overflow-x: auto;
    font-family: 'JetBrains Mono', 'Consolas', monospace;
    font-size: 0.85em;
    line-height: 1.5;
    margin: 1em 0;
    border-left: 4px solid #89b4fa;
}

pre code {
    background: none;
    padding: 0;
    border-radius: 0;
    font-size: inherit;
    color: inherit;
}

/* Inline code */
code {
    background: #e8e8f0;
    color: #c678dd;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', 'Consolas', monospace;
    font-size: 0.9em;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5em 0;
    font-size: 0.9em;
    table-layout: fixed;
    word-wrap: break-word;
}

thead {
    background: var(--color-table-header);
}

th {
    font-weight: 600;
    text-align: left;
    padding: 12px 16px;
    border: 1px solid var(--color-border);
    background: var(--color-table-header);
}

td {
    padding: 10px 16px;
    border: 1px solid var(--color-border);
    vertical-align: top;
}

tbody tr:nth-child(even) {
    background: var(--color-table-alt);
}

tbody tr:hover {
    background: #e8e8f0;
}

/* Lists */
ul, ol {
    margin: 0.8em 0;
    padding-left: 1.5em;
}

li { margin: 0.3em 0; }

/* Blockquote */
blockquote {
    border-left: 4px solid #89b4fa;
    margin: 1em 0;
    padding: 0.5em 1em;
    background: #f8f8fc;
    color: var(--color-muted);
}

blockquote p { margin: 0; }

/* Links */
a {
    color: #1e66f5;
    text-decoration: none;
}

/* Horizontal rule */
hr {
    border: none;
    border-top: 1px solid var(--color-border);
    margin: 2em 0;
}

/* Print adjustments */
@page {
    size: A4;
    margin: 20mm;
}

@media print {
    pre { break-inside: avoid; }
    table { break-inside: avoid; }
    h1, h2, h3 { break-after: avoid; }
}
</style>
"""

MARKDOWN_EXTENSIONS = ['tables', 'fenced_code', 'codehilite', 'nl2br', 'sane_lists']


def convert_md_to_pdf(md_path: str, pdf_path: str):
    if not Path(md_path).is_file():
        raise FileNotFoundError(f'Arquivo não encontrado: {md_path}')
    with open(md_path, encoding='utf-8') as f:
        html_content = markdown(f.read(), extensions=MARKDOWN_EXTENSIONS)
    html_with_font = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    {CSS_STYLES}
</head>
<body>
{html_content}
</body>
</html>"""
    HTML(string=html_with_font, base_url=Path(md_path).parent.as_posix()).write_pdf(pdf_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python render.py caminho/entrada.md caminho/saida.pdf")
        sys.exit(1)
    md_file, pdf_file = sys.argv[1], sys.argv[2]
    convert_md_to_pdf(md_file, pdf_file)
