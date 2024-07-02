from abc import ABC, abstractmethod

class EvaluationStrategy(ABC):
    @abstractmethod
    def evaluate(self, response: str) -> float:
        pass

class LengthEvaluationStrategy(EvaluationStrategy):
    def evaluate(self, response: str) -> float:
        return len(response)

class SentimentEvaluationStrategy(EvaluationStrategy):
    def evaluate(self, response: str) -> float:
        # Implementar a avaliação de sentimento
        return 0.0

class ResponseProcessor:
    def __init__(self, strategy: EvaluationStrategy):
        self.strategy = strategy

    def process(self, responses: list) -> list:
        return sorted(responses, key=self.strategy.evaluate, reverse=True)
