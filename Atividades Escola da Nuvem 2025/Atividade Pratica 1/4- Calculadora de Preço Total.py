# 4- Calculadora de Preço Total
#Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:
# Nome do produto: "Cadeira Infantil"
#Preço unitário: R$ 12.40
#Quantidade: 3 
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

def total(a, b):
    return(a * a)

preco_uni = 12.40
qtd = 3

print(f"O preço total do produto \"Cadeira Infantil\" é {total(preco_uni, qtd):.2f}")