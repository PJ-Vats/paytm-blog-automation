# CLAUDE.md — Paytm Blog Automation

Streamlit shell that serves HTML dashboards as fullscreen iframes. No Python logic.

| URL | HTML file | Page file |
|-----|-----------|-----------|
| `/` | `index.html` | `pages/home.py` |
| `/timeline` | `timeline.html` | `pages/timeline.py` |

Live: https://paytm-blog-automation.streamlit.app/ · Repo: https://github.com/PJ-Vats/paytm-blog-automation · **Deploy branch: `core/html` (NOT `main`)**

## Commands

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Architecture

```
streamlit_app.py   ← router: set_page_config + CSS + st.navigation + pg.run()
pages/home.py      ← renders index.html    → /
pages/timeline.py  ← renders timeline.html → /timeline
index.html / timeline.html  ← HTML source files (repo root)
requirements.txt   ← streamlit>=1.36.0
```

## Gotchas

### 1. Routing — `st.navigation`, never `pages/` auto-discovery
`pages/` dir silently ignored by Streamlit Cloud. Always register explicitly:

```python
pg = st.navigation(
    [
        st.Page("pages/home.py", title="Home"),
        st.Page("pages/timeline.py", title="Timeline", url_path="timeline"),
    ],
    position="hidden",  # hides sidebar nav widget
)
pg.run()
```

### 2. File paths — `__file__`-relative, never bare strings
CWD not guaranteed == repo root on Cloud for `pages/` scripts.

```python
ROOT = Path(__file__).parent.parent   # pages/foo.py → repo root
html_content = (ROOT / "timeline.html").read_text(encoding="utf-8")
# NOT: Path("timeline.html")  ← breaks on Cloud
```

### 3. `st.set_page_config` — router only
Only in `streamlit_app.py`. Calling in page files raises error when `st.navigation` active.

### 4. Fullscreen CSS — router injects once, applies everywhere

```css
/* Hide chrome */
#MainMenu, header, footer,
[data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }

/* Zero all padding layers (~6 nested divs) */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"],
[data-testid="block-container"], .main, .block-container,
section.main, section.main > div,
div[data-testid="stVerticalBlock"],
div[data-testid="stVerticalBlockBorderWrapper"] {
  padding: 0 !important; margin: 0 !important; max-width: 100% !important;
}

/* iframe fullscreen (st.components.v1.html always wraps in iframe) */
iframe { display: block; width: 100vw !important; height: 100vh !important; border: none !important; }
```

### 5. HTML wrapped in full document
`index.html`/`timeline.html` are fragments — page files wrap in `<!DOCTYPE html>` and inject CSS var defaults for light-mode iframe.

### 6. Deploy branch = `core/html`
`main` is behind — no `pages/` dir, no `st.navigation`. Push to `core/html`.

## Adding a New Page

1. Drop `foo.html` in repo root
2. Create `pages/foo.py`:

```python
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).parent.parent
html_content = (ROOT / "foo.html").read_text(encoding="utf-8")
full_page = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>:root{{--color-background-primary:#ffffff;--color-background-secondary:#f4f6f9;
--color-border-tertiary:rgba(15,23,42,.1);--color-text-primary:#0f172a;--color-text-secondary:#64748b;}}
html,body{{margin:0;padding:0;width:100%;height:100%;overflow-x:hidden;}}</style>
</head><body>{html_content}</body></html>"""
st.components.v1.html(full_page, height=900, scrolling=True)
```

3. Register in `streamlit_app.py`: `st.Page("pages/foo.py", title="Foo", url_path="foo")`

## Agents & Skills

| When | Use |
|------|-----|
| Before every PR | `pr-review-toolkit:code-reviewer` — iframe/CSS patterns break silently |
| Bad `Path()` read crashes page silently | `pr-review-toolkit:silent-failure-hunter` |
| Adding new pages / extending routing | `feature-dev:feature-dev` |
| 3+ pages added (shared wrapper duplication) | `code-simplifier` |
| After CSS/routing changes | `claude-md-management:revise-claude-md` — Streamlit changes `data-testid` attrs between versions |
