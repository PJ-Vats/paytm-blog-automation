import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Paytm Blog Automation – Timeline",
    layout="wide",
)

st.markdown(
    """
    <style>
      #MainMenu, header, footer { display: none !important; }

      html, body, [data-testid="stAppViewContainer"],
      [data-testid="stApp"], [data-testid="block-container"],
      .main, .block-container,
      section.main, section.main > div,
      div[data-testid="stVerticalBlock"],
      div[data-testid="stVerticalBlockBorderWrapper"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }

      iframe {
        display: block;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html_content = Path("timeline.html").read_text(encoding="utf-8")

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
