from datetime import datetime
import os
from langchain_core.runnables import RunnableConfig


def get_today_str() -> str:
    """Get current date in a human-readable format."""
    return datetime.now().strftime("%a %b %-d, %Y")
