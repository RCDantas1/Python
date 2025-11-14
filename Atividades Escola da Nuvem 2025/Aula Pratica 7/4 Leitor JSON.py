'''Crie um script em Python que leia e escreva dados em um arquivo JSON. 
O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.'''

import json

pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "São Paulo"
}

nome_arquivo = "pessoa.json"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

print("Dados gravados no arquivo JSON.")

# Ler dados do arquivo JSON
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)
    print(f"Nome: {dados_lidos['nome']} | Idade: {dados_lidos['idade']} | Cidade: {dados_lidos['cidade']}")
