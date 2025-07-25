import os
from cms_service.domain.services.search_engine import SearchEngine
from cms_service.infrastructure.services.search_engine_tavily import SearchEngineTavily
from cms_service.infrastructure.config import settings
from common.container.container import PunqContainer


container = PunqContainer()
tavily = SearchEngineTavily(api_key=settings.TAVILY_API_KEY)
container.register(SearchEngine, instance=tavily)
