from common.container.container import PunqContainer
from cms_service.infrastructure.di.services import register_services

container = PunqContainer()
register_services(container)
