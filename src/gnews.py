import os
import json
import httpx
import random
import json
import urllib.request
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools import tool

load_dotenv()

gnews_api_key=os.getenv('g_news')
google_api_key=os.getenv('google_api_key')


def get_gnews_stories() -> str:

    category = "technology"
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=us&max=10&apikey={gnews_api_key}"

    with urllib.request.urlopen(url) as response:
     data = json.loads(response.read().decode("utf-8"))
    articles = data["articles"]
    summaries = []

    for i,article in enumerate(articles):
       summaries.append(f"{i+1}.{article['title']}: {article['description']}")

    return "\n".join(summaries)

# gnews = get_gnews_stories()


# agent_data = Agent(
#     model=Gemini(id="gemini-2.0-flash",api_key=google_api_key),
#     tools=[gnews],
#     show_tool_calls=True,
#     markdown=True
# )

# agent = agent_data
# agent.print_response(f"Here are some news headlines:\n{gnews}\n\nSummarize these in bullet points.", stream=True)