
import streamlit as st
import requests
from datetime import datetime
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="BachatVikas - Financial News", page_icon=":newspaper:")
st.title("📰 BachatVikas - Financial News and AI Summaries")

# Dummy data for testing
news = {
    "title": "Govt terminates services of IMF ED K V Subramanian 6 months ahead of tenure",
    "pubDate": "2025-05-03 17:52:00",
    "image_url": "https://assets.thehansindia.com/h-upload/feeds/2021/10/07/1114078-kv-subramanian.jpg"
}

st.subheader(news["title"])
st.caption(f"🕒 {datetime.strptime(news['pubDate'], '%Y-%m-%d %H:%M:%S').strftime('%b %d, %Y %H:%M')}")

st.warning("The `use_column_width` parameter has been deprecated and replaced with `use_container_width`.")

# Load and display image safely
try:
    response = requests.get(news["image_url"])
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="News Image", use_container_width=True)
    else:
        st.error("❌ Unable to load image.")
except Exception as e:
    st.error(f"❌ Error loading image: {e}")
