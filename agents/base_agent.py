from  crewai import Agent

class BaseAgent(Agent):
    def __init__(self, role, goal, backstory, allow_delegation, verbose):
        super().__init__(
            role=role,
            goal=goal,
            backstory=backstory,
            allow_delegation=allow_delegation,
            verbose=verbose,
        )

    
    def execute(self):
        raise NotImplementedError("Each agent must implement its own execute method")
