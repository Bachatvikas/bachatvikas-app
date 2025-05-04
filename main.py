
import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="BachatVikas - Financial News", layout="wide")
st.markdown("# 📰 BachatVikas - Financial News and AI Summaries")

# Load news data from NewsData.io API (mocked for demonstration)
url = "https://newsdata.io/api/1/news?apikey=YOUR_API_KEY&category=business&language=en"
response = requests.get(url)
data = response.json()

if "results" in data:
    for news_item in data["results"]:
        st.subheader(news_item["title"])
        pub_date = news_item.get("pubDate", "")
        if pub_date:
            try:
                date_obj = datetime.strptime(pub_date, "%Y-%m-%d %H:%M:%S")
                st.caption(f"🕒 {date_obj.strftime('%B %d, %Y %H:%M')}")
            except ValueError:
                st.caption(f"🕒 {pub_date}")

        # Show warning if image is invalid or missing
        image_url = news_item.get("image_url", "")
        if image_url and image_url.startswith("http"):
            st.image(image_url, caption=news_item["title"], use_container_width=True)
        else:
            st.warning("No valid image available for this article.")

else:
    st.error("Failed to load news data. Please check your API key or network connection.")
