from crewai import Crew
from IPython.display import Markdown
from agents.market_research_agent import MarketResearchAgent
from tasks.research_task import research_task
topic=input("Enter the topic for market research: ")
market_research=MarketResearchAgent(topic=topic)
research_task=research_task(topic=topic)
crew=Crew(agents=[market_research], tasks=[research_task], verbose=True)

result=crew.kickoff()

print(Markdown(result))