import pandas as pd
import requests
import time

# Autor: Conceição Larissa Barbosa Ferreira
# Data de Criação: 20/07/2024
#
# Descrição:
# Este script é um bot para consultar informações de um CNPJ usando uma API pública.
# O usuário insere um CNPJ (apenas números) e o bot remove os caracteres especiais,
# faz uma requisição HTTP GET para a API, e imprime os dados retornados se a requisição for bem-sucedida.
# Em caso de falha na requisição, o bot informa o usuário que a verificação não foi possível.

def consultar_cnpj(cnpj):
    # Remove caracteres especiais do CNPJ e mantém os zeros à esquerda
    cnpj_limpo = ''.join(filter(str.isdigit, cnpj)).zfill(14)
    print(f"Consultando CNPJ: {cnpj_limpo}")
    
    url = f"https://publica.cnpj.ws/cnpj/{cnpj_limpo}"
    
    max_tentativas = 4
    tentativas = 0
    backoff_time = 21  
    
    while tentativas < max_tentativas:
        try:
            resp = requests.get(url)
            print(f"Status da requisição para {cnpj_limpo}: {resp.status_code}")
            if resp.status_code == 200:
                dados = resp.json()
                estabelecimento = dados.get('estabelecimento', {})
                razao_social = dados.get('razao_social', 'Não possui esse dado cadastrado')
                situacao_cadastral = estabelecimento.get('situacao_cadastral', 'Não possui esse dado cadastrado')
                cnpj_procurado = estabelecimento.get('cnpj', 'Não possui esse dado cadastrado')
                
                return cnpj_procurado, razao_social, situacao_cadastral
            elif resp.status_code == 429:
                print(f"Limite de requisições atingido para {cnpj_limpo}. Esperando {backoff_time} segundos.")
                time.sleep(backoff_time)
                backoff_time = min(backoff_time * 2, 60) 
                tentativas += 1
            else:
                print(f"Não foi possível verificar o CNPJ: {cnpj_limpo}")
                return cnpj, "Não foi possível verificar", "Não foi possível verificar"
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer a requisição para o CNPJ: {cnpj_limpo} - {e}")
            return cnpj, "Não foi possível verificar", "Não foi possível verificar"
    
    print(f"Não foi possível verificar o CNPJ: {cnpj_limpo} após {max_tentativas} tentativas.")
    return cnpj, "Não foi possível verificar", "Não foi possível verificar"

def processar_excel(input_file, output_file):
    df = pd.read_excel(input_file, dtype=str)  
    
    cnpjs_procurados = []
    razao_sociais = []
    situacoes_cadastrais = []
    
    for cnpj in df.iloc[:, 0]:
        cnpj_procurado, razao_social, situacao_cadastral = consultar_cnpj(cnpj)
        cnpjs_procurados.append(cnpj_procurado)
        razao_sociais.append(razao_social)
        situacoes_cadastrais.append(situacao_cadastral)
        
       
        time.sleep(21)
    
    df['CNPJ Procurado'] = cnpjs_procurados
    df['Razão Social'] = razao_sociais
    df['Situação Cadastral'] = situacoes_cadastrais
    
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    #Entrada de dados por excel
    input_file = r"C:\Estudos\Aprendizado_de_Python\CNPJ_BASE.xlsx" 
    #Saidade de dados criando um novo excel  
    output_file = r"C:\Estudos\Aprendizado_de_Python\CNPJ_Processados.xlsx"  
    processar_excel(input_file, output_file)