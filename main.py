import openai
from llm_connection import LLMConnectionFactory
from command import CLI, QueryCommand
from strategy import ResponseProcessor, LengthEvaluationStrategy
from observer import ResponseNotifier, ResponseObserver

# Defina sua chave de API da OpenAI aqui
openai.api_key = 'CHAVE API'

def main():
    # Inicialização da CLI
    cli = CLI()
    
    # Captura da entrada do usuário
    user_prompt = input("Digite sua pergunta: ")

    # Criação das conexões com os LLMs
    chatgpt_connection = LLMConnectionFactory.get_connection('chatgpt')
    another_llm_connection = LLMConnectionFactory.get_connection('another_llm')

    # Adicionar comandos com a entrada do usuário
    cli.add_command(QueryCommand(chatgpt_connection, user_prompt))
    cli.add_command(QueryCommand(another_llm_connection, user_prompt))

    # Executar comandos e obter respostas
    responses = cli.execute_commands()

    # Processar respostas usando uma estratégia de avaliação
    processor = ResponseProcessor(LengthEvaluationStrategy())
    sorted_responses = processor.process(responses)

    # Notificar observadores sobre a resposta escolhida
    notifier = ResponseNotifier()
    observer = ResponseObserver()
    notifier.attach(observer)

    # Escolher a melhor resposta (primeira da lista ordenada) e notificar
    best_response = sorted_responses[0]
    notifier.change_response(best_response)

    print(f"Melhor resposta: {best_response}")

if __name__ == "__main__":
    main()