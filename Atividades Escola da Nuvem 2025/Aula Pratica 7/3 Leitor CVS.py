'''Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. 
O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.'''

import csv

nome_arquivo = "dados_pessoais.csv" 

with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"Nome: {linha['Nome']} | Idade: {linha['Idade']} | Cidade: {linha['Cidade']}")
