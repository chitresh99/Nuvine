import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import json
import httpx
import random
import os 
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools import tool

load_dotenv()
news_api_key=os.getenv('News_api')
google_api_key=os.getenv('google_api_key')

newsapi = NewsApiClient(news_api_key)

def get_technews() -> str:
    top_headlines = newsapi.get_top_headlines(category='technology',
                                          language='en',
                                          country='us')

    articles = top_headlines["articles"]
    summaries = []

    for i,article in enumerate(articles):
         summaries.append(f"{i+1}. {article['title']} - {article['description']}")
    
    return "\n".join(summaries)


# technews = get_technews()
# agent_data = Agent(
#     model=Gemini(id="gemini-2.0-flash",api_key=google_api_key),
#     markdown=True
# )

# agent = agent_data
# agent.print_response(f"Here are some news headlines:\n{techcrunch}\n\nSummarize these in bullet points.", stream=True)