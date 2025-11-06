# 5- Calculadora de Número Inteiro
# Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
# Entrada: O arquivo de entrada contém 4 valores inteiros. 
# Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

def produto (a, b):
    return (a * b)

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
d = int(input("Digite o valor de D: "))

print(f"A diferença entre o produto de A e B e o produto de C e D é: {produto(a, b) - produto(c, d)}\n")