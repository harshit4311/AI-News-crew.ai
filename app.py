import streamlit as st
from agents import AINewsAgent
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("API_KEY")

# Initialize your agent with the API key
ai_news_agent = AINewsAgent(api_key)

# CSS for background color
st.markdown("""
    <style>
    .stApp {
        background-color: yellow;
    }
    .block-container {
        padding: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

def get_hot_ai_news():
    return ai_news_agent.get_hot_ai_news()

# Streamlit UI
st.title("Spicy AI News")
st.write("Get the hottest AI news on the fly!")

if st.button("Fetch AI News"):
    with st.spinner("Fetching news..."):
        news_list = get_hot_ai_news()
        if news_list:
            for news in news_list:
                st.write(f"**Title:** {news['title']}")
                st.write(f"[Link]({news['link']})")
        else:
            st.write("No AI news found.")
