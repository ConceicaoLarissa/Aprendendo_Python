# Autor: Conceição Larissa Barbosa Ferreira
# Data de Criação: 20/07/2024
#
# Descrição:
# Este script é um bot para consultar informações de um CNPJ usando uma API pública.
# O usuário insere um CNPJ (apenas números) e o bot remove os caracteres especiais,
# faz uma requisição HTTP GET para a API, e imprime os dados retornados se a requisição for bem-sucedida.
# Em caso de falha na requisição, o bot informa o usuário que a verificação não foi possível.

import requests

def consultar_cnpj(cnpj):
    # Remove caracteres especiais do CNPJ
    cnpj_limpo = ''.join(filter(str.isdigit, cnpj))
    
    url = f"https://publica.cnpj.ws/cnpj/{cnpj_limpo}"
    
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            dados = resp.json()
            print(dados)
        else:
            print("Não foi possível verificar")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        print("Não foi possível verificar")

if __name__ == "__main__":
    cnpj = input("Digite o CNPJ (somente números): ")
    consultar_cnpj(cnpj)