import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Uzum Market Analog",
    page_icon="🛒",
    layout="wide"
)

html_file = Path("indexw.html")

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")

    components.html(
        html_content,
        height=2500,
        scrolling=True
    )
else:
    st.error("indexw.html fayli topilmadi!")
    st.write("Repository ichida indexw.html mavjudligini tekshiring.")