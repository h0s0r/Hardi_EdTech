# Importing Required Modules/Libraries

from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
import os

# loading API Key's from .env using dotenv
load_dotenv()

# TOOL 1 - Tavily Tool

def get_tavily_tool():
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("Tavily API Key not found.")
    return TavilySearchResults(api_key=api_key)
