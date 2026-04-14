from pathlib import Path
import streamlit as st

ROOT = Path(__file__).parent.parent
html_content = (ROOT / "index.html").read_text(encoding="utf-8")

full_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  :root {{
    --color-background-primary: #ffffff;
    --color-background-secondary: #f4f6f9;
    --color-border-tertiary: rgba(15,23,42,.1);
    --color-text-primary: #0f172a;
    --color-text-secondary: #64748b;
  }}
  html, body {{ margin: 0; padding: 0; width: 100%; height: 100%; background: var(--color-background-primary); overflow-x: hidden; }}
</style>
</head>
<body>
{html_content}
</body>
</html>"""

st.components.v1.html(full_page, height=900, scrolling=True)
