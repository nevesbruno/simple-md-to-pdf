import sys
from pathlib import Path
from markdown import markdown
from weasyprint import HTML

GOOGLE_FONTS_CSS = (
    '<link href="https://fonts.googleapis.com/css?family=Poppins:400,700&display=swap" rel="stylesheet">\n'
    '<style>body { font-family: \"Poppins\", sans-serif; }</style>'
)

def convert_md_to_pdf(md_path: str, pdf_path: str):
    if not Path(md_path).is_file():
        raise FileNotFoundError(f'Arquivo não encontrado: {md_path}')
    with open(md_path, encoding='utf-8') as f:
        html_content = markdown(f.read())
    html_with_font = f"""
    <html>
    <head>{GOOGLE_FONTS_CSS}</head>
    <body>{html_content}</body>
    </html>
    """
    HTML(string=html_with_font, base_url=Path(md_path).parent.as_posix()).write_pdf(pdf_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python render.py caminho/entrada.md caminho/saida.pdf")
        sys.exit(1)
    md_file, pdf_file = sys.argv[1], sys.argv[2]
    convert_md_to_pdf(md_file, pdf_file)
