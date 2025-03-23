from tasks.base_task import BaseTask
from agents.idea_viability_agent import IdeaViabilityAgent

class IdeaViabilityTask(BaseTask):
    def __init__(self, idea):
        super().__init__(
            topic=idea,
            description=f"Analyze the viability of the idea {idea} and provide insights to the team",
            expected_output="Idea viability report with recommendations",
            agent=IdeaViabilityAgent(idea=idea)
        )