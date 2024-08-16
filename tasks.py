import requests

class SearchTask:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_ai_news(self, query="AI news"):
        url = "https://serpapi.com/search"
        params = {
            "q": query,
            "api_key": self.api_key,
        }
        response = requests.get(url, params=params)
        return response.json()
