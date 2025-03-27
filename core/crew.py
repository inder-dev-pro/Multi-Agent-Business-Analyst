from crewai import Crew, Process
from IPython.display import Markdown
from agents.idea_viability_agent import IdeaViabilityAgent
from tasks.idea_viability_task import IdeaViabilityTask
from agents.market_research_agent import MarketResearchAgent
from tasks.research_task import research_task
from agents.funding_advisor_agent import FundingAdvisorAgent
from tasks.funding_task import FundingTask
from dotenv import load_dotenv
import sys

load_dotenv(r"config\.env")

try:
    user_input = int(input("What do you want to do?\n1. Market Research\n2. Idea Viability\n3. Funding Analysis\n4. All of the above\n"))
    if user_input == 1:
        topic = input("Enter the topic for market research: ")
        market_research = MarketResearchAgent(topic=topic)
        market_research_task = research_task(topic=topic)
        crew = Crew(agents=[market_research], tasks=[market_research_task], verbose=True, Process=Process.sequential)
    elif user_input == 2:
        idea = input("Enter the idea for viability analysis: ")
        idea_viability = IdeaViabilityAgent(idea=idea)
        idea_viability_task = IdeaViabilityTask(idea=idea)
        crew = Crew(agents=[idea_viability], tasks=[idea_viability_task], verbose=True, Process=Process.sequential)
    elif user_input == 3:
        idea = input("Enter the idea for funding analysis: ")
        funding_advisor = FundingAdvisorAgent(idea=idea)
        funding_advisor_task = FundingTask(idea=idea)
        crew = Crew(agents=[funding_advisor], tasks=[funding_advisor_task], verbose=True, Process=Process.sequential)
    elif user_input == 4:
        topic = input("Enter the topic for market research: ")
        idea = input("Enter the idea for viability analysis: ")
        fund = input("Enter the idea for funding analysis: ")
        idea_viability = IdeaViabilityAgent(idea=idea)
        idea_viability_task = IdeaViabilityTask(idea=idea)
        market_research = MarketResearchAgent(topic=topic)
        market_research_task = research_task(topic=topic)
        funding_advisor = FundingAdvisorAgent(idea=idea)
        funding_advisor_task = FundingTask(idea=idea)
        crew = Crew(
            agents=[market_research, idea_viability, funding_advisor],
            tasks=[market_research_task, idea_viability_task, funding_advisor_task],
            verbose=True,
            Process=Process.sequential
        )
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
        sys.exit(1)

    # Execute the crew process
    result = crew.execute()
    print(Markdown(result))

except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")