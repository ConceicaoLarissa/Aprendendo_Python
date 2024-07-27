# Aprendizado_de_Python

Pequenas coisas que estou aprendendo com python

# Bots de Consulta de CNPJ

## Descrição

Este repositório contém scripts para consultar informações de CNPJ usando uma API pública. Os scripts têm as seguintes funcionalidades:

1. **Consulta Simples de CNPJ**: Solicita um CNPJ ao usuário, remove os caracteres especiais e faz uma requisição HTTP GET para a API pública. Imprime os dados retornados ou uma mensagem de erro se a requisição falhar.

2. **Consulta de CNPJ com Processamento de Excel**: Lê um arquivo Excel contendo uma coluna de CNPJs, consulta cada CNPJ usando a API, e salva os resultados em um novo arquivo Excel. Inclui tratamento de erros e uma estratégia de backoff em caso de limite de requisições atingido.

## Ferramentas e Tecnologias

- **Linguagem**: Python
- **Bibliotecas**:
  - `requests`: Para fazer requisições HTTP para a API.
  - `pandas`: Para manipulação e processamento de arquivos Excel.
- **API**: Publica CNPJ (https://publica.cnpj.ws)

## Requisitos

Para executar os scripts, você precisa ter o Python instalado e as seguintes bibliotecas Python:

- `requests`
- `pandas`

Você pode instalar as bibliotecas necessárias com o seguinte comando:

```sh
pip install requests pandas

```
