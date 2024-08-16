from agents import AINewsAgent

def main():
    api_key = "e0bd2bbdb5ba96f17964ce559e9d1325362075b4670fae503dacdb2339952bb8" 
    ai_news_agent = AINewsAgent(api_key)
    
    hot_ai_news = ai_news_agent.get_hot_ai_news()

    if hot_ai_news:
        for news in hot_ai_news:
            print(f"Title: {news['title']}")
            print(f"Link: {news['link']}")
            print()
    else:
        print("No AI news found.")

if __name__ == "__main__":
    main()
