from cms_service.infrastructure.services.search_engine_tavily import SearchEngineTavily
from cms_service.infrastructure.config import settings
from cms_service.domain.services.search_engine import SearchEngine
from common.container.container import IContainer


def register_services(container: IContainer):
    container.register(SearchEngine, factory=lambda: SearchEngineTavily(api_key=settings.TAVILY_API_KEY))
