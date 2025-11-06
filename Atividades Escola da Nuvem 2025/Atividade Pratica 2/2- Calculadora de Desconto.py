'''2- Calculadora de Desconto 
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.'''

preco = float(input("Digite o valor do produto: "))
desconto = float(preco * 0.2)
print("Concedemos um desconto de", desconto, "e o preço final do produto é de", (preco - desconto))
