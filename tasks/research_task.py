from tasks.base_task import BaseTask
from agents.market_research_agent import MarketResearchAgent
class research_task(BaseTask):
    def __init__(self):
        super().__init__(
            description="Analyze the market and provide insights to the team for {topic}",
            expected_output="Market analysis report with key insights and recommendations",
            agent=MarketResearchAgent()
        )