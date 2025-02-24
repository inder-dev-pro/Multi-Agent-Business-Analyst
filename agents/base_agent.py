from  crewai import Agent

class BaseAgent(Agent):
    def __init__(self, name):
        super().__init__(name=name)
    
    def execute(self, startup_data):
        raise NotImplementedError("Each agent must implement its own execute method")
