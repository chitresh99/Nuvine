import json
import httpx
import random
import os 
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools import tool

load_dotenv()
api_key=os.getenv('google_api_key')

def get_top_hackernews_stories(num_stories: int = 10) -> str:
  
    response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = response.json()

    
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)

agent_data = Agent(
    model=Gemini(id="gemini-2.0-flash",api_key=api_key),
    tools=[get_top_hackernews_stories],
    show_tool_calls=True,
    markdown=True
)

agent = agent_data
agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)