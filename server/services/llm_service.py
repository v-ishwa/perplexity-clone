import google.generativeai as genai


class LLMService:
    def __init__(self):
        self.model = genai.GenerativeModel()

    def generate_response(self, query: str, search_results: list) -> str:

        return f"Generated response for query: '{query}' with {len(search_results)} search results."
