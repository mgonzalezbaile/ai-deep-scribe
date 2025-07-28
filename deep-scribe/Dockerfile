FROM python:3.13-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install Node.js for BAML CLI and git for foundry
RUN apt-get update && apt-get install -y curl git && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Install BAML CLI globally
RUN npm install -g @boundaryml/baml

# Set the working directory.
WORKDIR /app

# Install the application dependencies.
COPY uv.lock pyproject.toml ./
RUN uv sync --frozen --no-cache

# Copy the rest of the application into the container.
COPY ./src/ src/

# Copy the tests directory to access fixture data
COPY ./tests/ tests/

# Compile BAML files to generate baml_client
WORKDIR /app/src/cms_service/domain/prompts
RUN baml-cli generate

# Go back to app directory
WORKDIR /app

# Set PYTHONPATH so Python can find the cms_service module
ENV PYTHONPATH=/app/src
ENV PROJECT_ROOT_PATH=/app

CMD ["/app/.venv/bin/fastapi", "run", "/app/src/cms_service/infrastructure/api.py", "--port", "8000", "--host", "0.0.0.0"]
