import streamlit as st

st.set_page_config(
    page_title="Paytm Blog Automation",
    layout="wide",
)

# Strip ALL Streamlit chrome — runs on every page load (router always executes)
st.markdown(
    """
    <style>
      #MainMenu, header, footer,
      [data-testid="stSidebar"],
      [data-testid="stSidebarNav"] { display: none !important; }

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

pg = st.navigation(
    [
        st.Page("pages/home.py", title="Home"),
        st.Page("pages/timeline.py", title="Timeline", url_path="timeline"),
    ],
    position="hidden",
)
pg.run()
