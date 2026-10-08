from tavily import TavilyClient
from config.config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(query):

    results = client.search(query)

    snippets = []

    for r in results["results"][:3]:
        snippets.append(r["content"])

    return snippets