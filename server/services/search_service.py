from config import Settings
from tavily import TavilyClient
import trafilatura

settings = Settings()
tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)


class SearchService:
    def web_search(self, query: str):
        results = []
        response = tavily_client.search(query, max_results=10)
        search_results = response.get("results", [])

        for result in search_results:
            try:
                downloaded = trafilatura.fetch_url(result.get("url", ""))
                if downloaded is None:
                    continue
                content = trafilatura.extract(downloaded, include_comments=False)
                if content is None:
                    content = "Could not extract content"
                results.append(
                    {
                        "title": result.get("title", ""),
                        "url": result.get("url", ""),
                        "content": content,
                    }
                )
            except Exception as e:
                print(f"Error processing {result.get('url', '')}: {str(e)}")
                continue
        return results
