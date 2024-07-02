from abc import ABC, abstractmethod
import openai

class LLMConnection(ABC):
    @abstractmethod
    def query(self, prompt: str) -> str:
        pass

class ChatGPTConnection(LLMConnection):
    def query(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()

class AnotherLLMConnection(LLMConnection):
    def query(self, prompt: str) -> str:
        # Implementar a chamada à API de outro LLM
        # Por exemplo, você pode usar uma API simulada ou outra biblioteca
        return "Resposta de outro LLM"

class LLMConnectionFactory:
    @staticmethod
    def get_connection(llm_type: str) -> LLMConnection:
        if llm_type == 'chatgpt':
            return ChatGPTConnection()
        elif llm_type == 'another_llm':
            return AnotherLLMConnection()
        else:
            raise ValueError(f"Unknown LLM type: {llm_type}")