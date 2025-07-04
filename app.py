import streamlit as st
from streamlit.components.v1 import html
import base64

# Set page configuration
st.set_page_config(
    page_title="EduHelper - AI Homework Assistance",
    page_icon="📚",
    layout="wide"
)

# Read the HTML content from file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display the HTML app
html(html_content, width=1000, height=1000, scrolling=True)

# Add Streamlit analytics (optional)
st.markdown("""<script async src="https://cdn.splitbee.io/sb.js"></script>""", unsafe_allow_html=True)
