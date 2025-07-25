import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent.parent / ".env", extra="ignore", env_file_encoding="utf-8"
    )

    # --- Comet ML & Opik Configuration ---
    COMET_API_KEY: str | None = Field(default=None, description="API key for Comet ML and Opik services.")
    COMET_PROJECT: str = Field(
        default="incident_analysis",
        description="Project name for Comet ML and Opik tracking.",
    )

    # --- LLM Configuration ---
    LLM_MODEL: str = Field(
        description="Model name for the LLM.",
    )

    # --- OpenRouter Configuration ---
    OPENROUTER_API_KEY: str = Field(
        description="API key for the OpenRouter service.",
    )

    TAVILY_API_KEY: str = Field(
        description="API key for the Tavily service.",
    )

    MAX_SUBTOPICS: int = Field(
        default=2,
        description="Maximum number of subtopics to generate.",
    )

    MAX_SEARCH_RESULTS: int = Field(
        default=3,
        description="Maximum number of search results to return.",
    )


settings = Settings()
