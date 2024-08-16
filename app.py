import streamlit as st
from agents import AINewsAgent

# Initialize your agent with the API key
api_key = "e0bd2bbdb5ba96f17964ce559e9d1325362075b4670fae503dacdb2339952bb8"
ai_news_agent = AINewsAgent(api_key)

# CSS for background color
st.markdown("""
    <style>
    body {
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
st.write("Get the hottest AI news on the fly! ")

if st.button("Fetch AI News"):
    with st.spinner("Fetching news..."):
        news_list = get_hot_ai_news()
        if news_list:
            for news in news_list:
                st.write(f"**Title:** {news['title']}")
                st.write(f"[Link]({news['link']})")
        else:
            st.write("No AI news found.")
