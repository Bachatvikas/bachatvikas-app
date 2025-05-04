import streamlit as st
import requests
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="BachatVikas - Financial News", layout="wide")

# App title
st.title("📰 BachatVikas - Financial News Feed")

# Disclaimer
with st.expander("Disclaimer"):
    st.markdown("""
    This website provides publicly available financial news via NewsData.io.  
    We do not claim ownership of any news content. All trademarks and copyrights belong to their respective owners.  
    This platform is for informational purposes only and not financial advice.
    """)

# NewsData.io API Key
API_KEY = "pub_846177a12be625569a426a1700c422da6e055"

# Define the endpoint
url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&category=business&language=en"

# Make the API request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if "results" in data:
        for news_item in data["results"]:
            st.markdown("---")
            st.subheader(news_item.get("title", "No Title"))

            # Date formatting
            pub_date = news_item.get("pubDate", "")
            if pub_date:
                try:
                    date_obj = datetime.strptime(pub_date, "%Y-%m-%d %H:%M:%S")
                    st.caption(f"🕒 {date_obj.strftime('%B %d, %Y %H:%M')}")
                except ValueError:
                    st.caption(f"🕒 {pub_date}")

            # Image handling
            image_url = news_item.get("image_url", "")
            if image_url and image_url.startswith("http"):
                try:
                    st.image(image_url, caption=news_item["title"], use_container_width=True)
                except:
                    st.warning("⚠️ Unable to display image.")
            else:
                st.info("📷 No image available.")

            # Description or content
            description = news_item.get("description") or news_item.get("content")
            if description:
                st.write(description)
            else:
                st.write("No description available.")
    else:
        st.warning("No news results found.")
else:
    st.error("Failed to fetch news data. Please check your API key or network.")

