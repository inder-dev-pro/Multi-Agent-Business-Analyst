from tasks.base_task import BaseTask
from agents.market_research_agent import MarketResearchAgent

class MarketResearchTask(BaseTask):
    def __init__(self, topic):
        super().__init__(
            topic=topic,
            description=f"Analyze the market and provide insights to the team for {topic}",
            expected_output="Market analysis report with key insights and recommendations",
            agent=MarketResearchAgent(topic=topic)
        )