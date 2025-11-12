'''Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, 
além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.'''

import requests

codigo = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{codigo}-BRL"
resposta = requests.get(url)
if resposta.status_code == 200:
    key = f"{codigo}BRL"
    dados = resposta.json().get(key, {})
    if dados:
        print(f"Valor atual: {dados.get('bid', 'N/A')}")
        print(f"Valor máximo: {dados.get('high', 'N/A')}")
        print(f"Valor mínimo: {dados.get('low', 'N/A')}")
        print(f"Data/hora: {dados.get('create_date', 'N/A')}")
    else:
        print("Moeda não encontrada ou código inválido.")
else:
    print("Erro ao consultar a cotação.")
