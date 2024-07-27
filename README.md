# Aprendizado_de_Python
 Pequenas coisas que estou aprendendo com python 

# Bots de Consulta de CNPJ

## Descrição

Este repositório contém scripts para consultar informações de CNPJ usando uma API pública. Os scripts têm as seguintes funcionalidades:

1. **Consulta Simples de CNPJ**: Consulta um CNPJ fornecido pelo usuário e imprime os dados retornados pela API.
2. **Consulta de CNPJ com Processamento de Excel**: Lê um arquivo Excel com CNPJs, consulta cada CNPJ usando a API e salva os resultados em um novo arquivo Excel.

## Scripts

### 1. Consulta Simples de CNPJ

- **Arquivo**: `consulta_cnpj_simples.py`
- **Descrição**: Este script solicita um CNPJ ao usuário, remove os caracteres especiais, e faz uma requisição HTTP GET para a API pública. Imprime os dados retornados ou uma mensagem de erro se a requisição falhar.
