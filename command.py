from abc import ABC, abstractmethod
from llm_connection import LLMConnection

class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass

class QueryCommand(Command):
    def __init__(self, connection: LLMConnection, prompt: str):
        self.connection = connection
        self.prompt = prompt

    def execute(self) -> str:
        return self.connection.query(self.prompt)

class CLI:
    def __init__(self):
        self.commands = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def execute_commands(self):
        results = []
        for command in self.commands:
            results.append(command.execute())
        return results
