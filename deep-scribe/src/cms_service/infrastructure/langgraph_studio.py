from cms_service.infrastructure.di.di import bootstrap


def get_create_post_graph():
    """
    Bootstraps the DI container and returns the compiled 'create_post_graph'.

    This function serves as the entrypoint for the langgraph-api, ensuring that
    all services and graph dependencies are properly initialized and injected.
    """
    container = bootstrap()
    return container.get("create_post_graph")
