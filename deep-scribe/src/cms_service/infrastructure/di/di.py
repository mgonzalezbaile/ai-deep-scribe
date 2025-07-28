from common.container.container import IContainer, PunqContainer
from cms_service.infrastructure.di.services import register_services


def bootstrap() -> IContainer:
    container = PunqContainer()
    register_services(container)

    return container
