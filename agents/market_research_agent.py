import os
from groq import Groq
from agents.base_agent import BaseAgent
from dotenv import load_dotenv
load_dotenv(r"config\.env")
OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]
'''load_dotenv(r"config\.env")
GROQ_API_KEY=os.environ["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)'''
class MarketResearchAgent(BaseAgent):
    def __init__(self, topic):
        super().__init__(
            role="Market_Researcher",
            goal=f"To analyze the market and provide insights about {topic} to the team",
            backstory=  "I am a market researcher who has been working in the industry for several years."
                        "I have experience in analyzing market trends, consumer behavior, and competitive landscapes."
                        "My goal is to provide valuable insights to the team to help them make informed decisions and develop successful strategies."
                        "I am passionate about understanding the market and identifying opportunities for growth."
                        "I am excited to work with the team and contribute to the success of the project.",
            allow_delegation=False,
            verbose=True,
        
            )
