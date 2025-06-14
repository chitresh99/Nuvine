import json
import httpx
import random
import requests
import json
import os 
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools import tool

load_dotenv()
api_key=os.getenv('google_api_key')

hackernews_top_stories="https://hacker-news.firebaseio.com/v0/topstories.json"
hackernews_items="https://hacker-news.firebaseio.com/v0/item/{}.json"

def get_top_story_id(limit=10):
    response = requests.get(hackernews_top_stories)
    if response.status_code == 200:
        return response.json()[:limit]
    else:
        print("Failed to search")
        return[]
    
def get_story_details(story_id):
    response = requests.get(hackernews_items.format(story_id))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch story {story_id}")
        return None

def get_news(limit=10):
    story_ids = get_top_story_id(limit)
    stories_output = []
    for i, story_id in enumerate(story_ids, start=1):
        story = get_story_details(story_id)
        if story:
            entry = f"{i}. {story.get('title')}\n    URL: {story.get('url', 'No URL')}\n    Score: {story.get('score')}, Comments: {story.get('descendants', 0)}\n"
            stories_output.append(entry)
    return "\n".join(stories_output)

# agent_data = Agent(
#     model=Gemini(id="gemini-2.0-flash",api_key=api_key),
#     markdown=True
# )

# headlines = get_news(limit=10)
# agent = agent_data
# agent.print_response(f"Here are some news headlines:\n{get_news(limit=10)}\n\nSummarize these in bullet points.", stream=True)

