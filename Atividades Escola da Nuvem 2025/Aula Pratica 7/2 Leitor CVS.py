Crie um script em Python que escreva dados em um arquivo CSV. 
O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.

import csv

pessoas = [
    {"Nome": "João", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Maria", "Idade": 30, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carlos", "Idade": 22, "Cidade": "Belo Horizonte"}
]


nome_arquivo = "dados_pessoais.csv"


with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
    campos = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()  
    for pessoa in pessoas:
        escritor.writerow(pessoa)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
