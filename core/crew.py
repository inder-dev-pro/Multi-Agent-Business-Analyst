from crewai import Crew
from IPython.display import Markdown
from agents.idea_viability_agent import IdeaViabilityAgent
from tasks.idea_viability_task import IdeaViabilityTask
from agents.market_research_agent import MarketResearchAgent
from tasks.research_task import research_task
topic=input("Enter the topic for market research: ")
idea=input("Enter the idea for viability analysis: ")
idea_viability=IdeaViabilityAgent(idea=idea)
idea_viability_task=IdeaViabilityTask(idea=idea)
market_research=MarketResearchAgent(topic=topic)
research_task=research_task(topic=topic)
crew=Crew(agents=[idea_viability], tasks=[idea_viability_task], verbose=True)

result=crew.kickoff()

print(Markdown(result))