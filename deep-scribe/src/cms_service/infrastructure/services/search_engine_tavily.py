from typing import List
from cms_service.domain.services.search_engine import SearchEngine
from tavily import AsyncTavilyClient
from cms_service.domain.services.search_engine import SearchResult


class SearchEngineTavily(SearchEngine):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = AsyncTavilyClient(api_key=api_key)

    async def search(self, query: str, max_results: int = 10) -> List[SearchResult]:
        response = await self.client.search(query, max_results=max_results, include_raw_content=False, topic="general")
        unique_results = {}
        for result in response["results"]:
            url = result["url"]
            if url not in unique_results:
                unique_results[url] = {**result, "query": response["query"]}

        return [SearchResult(**result) for result in unique_results.values()]
