# 3- Calculadora de Volume
# Crie um programa que calcule o volume de uma caixa retangular. Use as seguintes dimensões:
#Comprimento: 12 cm
#Largura: 14 cm
#Altura: 20 cm 
#O programa deve calcular o volume e exibir o resultado em cm³.

def volume (a, b, c):
    return a * b * c

comprimento = 12 
largura = 14 
altura = 20

print(f"O volume da caixa é {volume(comprimento, largura, altura)} m³")