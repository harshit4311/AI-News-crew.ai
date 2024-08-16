from tasks import SearchTask

class AINewsAgent:
    def __init__(self, api_key):
        self.search_task = SearchTask(api_key)

    def get_hot_ai_news(self, num_results=10):
        results = self.search_task.search_ai_news()

        # Debug: Print the entire response to see what's returned
        print("API Response:", results)

        # Extract the titles and URLs of the related questions if no news results
        news_list = []
        related_questions = results.get('related_questions', [])
        if related_questions:
            for question in related_questions:
                news_list.append({
                    "title": question.get("title"),
                    "link": question.get("link"),
                })
        else:
            print("No news or related questions found.")
        return news_list