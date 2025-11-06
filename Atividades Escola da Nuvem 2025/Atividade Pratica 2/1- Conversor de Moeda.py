''' 1- Conversor de Moeda 
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.60
Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.'''

def dolar (x):
    return x * 5.60

def euro (x):
    return x * 6.60

real = float(input("Digite o valor em reais: "))
print("Valor convertido em dolar:", (dolar(real)))
print("Valor convertido em EURO: ", euro(real))
