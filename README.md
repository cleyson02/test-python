# Multi-LLM Query System

Este projeto é uma aplicação Python que permite a conexão com múltiplos Modelos de Linguagem (LLMs) para gerar respostas a partir de prompts fornecidos pelo usuário. Ele utiliza o padrão de projeto Command para gerenciar comandos e o padrão de projeto Strategy para avaliar as respostas, além de implementar o padrão Observer para notificação de mudanças nas respostas.

## Funcionalidades

1. **Conexão com múltiplos LLMs**: Conecta-se ao ChatGPT e a outro LLM fictício para gerar respostas.
2. **Execução de Comandos**: Usa o padrão Command para encapsular comandos que consultam os LLMs.
3. **Avaliação de Respostas**: Implementa estratégias de avaliação de respostas, como o comprimento da resposta.
4. **Notificação de Mudanças**: Utiliza o padrão Observer para notificar sobre a mudança de respostas.

## Configuração

### Pré-requisitos

1. Python 3.7 ou superior.
2. Biblioteca `openai` para conexão com o ChatGPT.
3. Chave de API da OpenAI.

### Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install openai
    ```

4. Defina sua chave de API da OpenAI no código. Substitua `'CHAVE API'` pela sua chave de API:
    ```python
    openai.api_key = 'CHAVE API'
    ```

## Estrutura do Projeto

- `command.py`: Implementa os comandos para consulta aos LLMs.
- `llm_connection.py`: Define as conexões com os LLMs (ChatGPT e um LLM fictício).
- `observer.py`: Implementa o padrão Observer para notificação de mudanças nas respostas.
- `strategy.py`: Define estratégias de avaliação das respostas.
- `main.py`: O ponto de entrada do programa.

## Execução

1. No terminal, navegue até o diretório do projeto.
2. Execute o programa:
    ```sh
    python main.py
    ```

3. Digite sua pergunta quando solicitado:
    ```sh
    Digite sua pergunta: 
    ```

4. O programa executará as consultas aos LLMs, avaliará as respostas e notificará a melhor resposta:
    ```sh
    Melhor resposta: [Resposta escolhida]
    ```

## Detalhes das Funcionalidades

### Conexão com Múltiplos LLMs

O projeto permite a conexão com diferentes LLMs. Atualmente, está implementado para conectar-se ao ChatGPT e a um LLM fictício.

### Execução de Comandos

Usa o padrão Command para encapsular as ações de consulta aos LLMs. Os comandos são adicionados a uma lista na classe `CLI` e executados sequencialmente.

### Avaliação de Respostas

Utiliza o padrão Strategy para avaliar as respostas. A estratégia de avaliação atual é baseada no comprimento da resposta (`LengthEvaluationStrategy`). Outras estratégias, como avaliação de sentimento, podem ser implementadas facilmente.

### Notificação de Mudanças

Implementa o padrão Observer para notificar mudanças nas respostas. A classe `ResponseNotifier` notifica os observadores sobre a mudança de resposta, garantindo que todas as partes interessadas sejam informadas.

## Customização

### Adicionar Novo LLM

Para adicionar um novo LLM, siga os passos abaixo:

1. Crie uma nova classe que herde de `LLMConnection` e implemente o método `query`.
2. Adicione um novo caso no método `get_connection` da classe `LLMConnectionFactory`.

### Adicionar Nova Estratégia de Avaliação

Para adicionar uma nova estratégia de avaliação, siga os passos abaixo:

1. Crie uma nova classe que herde de `EvaluationStrategy` e implemente o método `evaluate`.
2. Utilize a nova estratégia ao instanciar `ResponseProcessor`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).