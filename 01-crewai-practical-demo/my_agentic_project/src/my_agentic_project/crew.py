from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MyAgenticProject():
    """MyAgenticProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def market_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['market_researcher'],
            verbose=True
        )
    
    @agent
    def content_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['content_strategist'],
            verbose=True
        )
    
    @agent
    def technical_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_writer'],
            verbose=True
        )
    
    @agent
    def creative_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_writer'],
            verbose=True
        )
    

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            output_file='multi-agent-report.md'
        )
    
    @task
    def content_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_strategy_task'],
            output_file='content_stratregy.md'
        )
    
    @task
    def technical_documentation_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_documentation_task'],
            output_file='technical_documentation.md'
        )
    
    @task
    def creative_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['creative_content_task'],
            output_file='creative_content.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MyAgenticProject crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            verbose=True,
        )
