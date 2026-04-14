import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Paytm Blog Automation",
    layout="wide",
)

# Remove default Streamlit padding so the HTML widget fills the viewport
st.markdown(
    "<style>section.main > div { padding: 0 !important; } </style>",
    unsafe_allow_html=True,
)

html_content = Path("index.html").read_text(encoding="utf-8")

# Wrap the fragment in a full HTML page with CSS variable defaults so the
# component renders correctly in Streamlit's light-mode iframe.
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
  body {{ margin: 0; padding: 0; background: var(--color-background-primary); }}
</style>
</head>
<body>
{html_content}
</body>
</html>"""

st.components.v1.html(full_page, height=900, scrolling=True)
