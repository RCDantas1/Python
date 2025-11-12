'''Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. 
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.'''

import requests

cep = input("Digite o CEP (apenas números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
if resposta.status_code == 200:
    dados = resposta.json()
    if "erro" not in dados:
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados.get('bairro', 'N/A')}")
        print(f"Cidade: {dados.get('localidade', 'N/A')}")
        print(f"Estado: {dados.get('uf', 'N/A')}")
    else:
        print("CEP não encontrado.")
else:
    print("Erro ao consultar o CEP.")
