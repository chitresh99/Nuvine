from src.gnews import get_gnews_stories
from src.technews import get_technews
from src.hackernews import get_news

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools import tool

import os
from dotenv import load_dotenv

load_dotenv()
google_api_key=os.getenv('google_api_key')

gnews=get_gnews_stories()
technews=get_technews()
hackernews=get_news(limit=10)

agent_data = Agent(
        model=Gemini(id="gemini-2.0-flash",api_key=google_api_key),
        markdown=True
)
agent = agent_data
agent.print_response(f"Here are some news headlines:\n{hackernews,gnews,technews}\n\nSummarize these in bullet points.", stream=True)




