import os
from groq import GROQ
from agents.base_agent import BaseAgent
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY=os.environ["GROQ_API_KEY"]
class MarketResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Market_Researcher",
            goal="To analyze the market and provide insights about {topic} to the team",
            backstory=  "I am a market researcher who has been working in the industry for several years."
                        "I have experience in analyzing market trends, consumer behavior, and competitive landscapes."
                        "My goal is to provide valuable insights to the team to help them make informed decisions and develop successful strategies."
                        "I am passionate about understanding the market and identifying opportunities for growth."
                        "I am excited to work with the team and contribute to the success of the project.",
            allow_delegation=False,
            verbose=True,
            llm=GROQ(api_key=GROQ_API_KEY)
            )
