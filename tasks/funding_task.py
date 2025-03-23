from tasks.base_task import BaseTask
from agents.funding_advisor_agent import FundingAgent

class FundingTask(BaseTask):
    def __init__(self, idea):
        super().__init__(
            topic=idea,
            description=f"Analyze the funding options for {idea} and provide recommendations",
            expected_output="Funding report with recommendations",
            agent=FundingAgent(idea=idea)
        )
