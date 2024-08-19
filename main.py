from agents import AINewsAgent

def main():
    api_key = "9e92b6fe16a1820edfaaa5253e33692509d6f5721cac4cebecf82329dd06a29f" 
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
