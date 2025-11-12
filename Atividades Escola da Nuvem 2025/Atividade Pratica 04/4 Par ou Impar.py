'''Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. 
Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.'''

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
    if entrada.lower() == 'fim':
        break
    try:
        num = int(entrada)
        if num % 2 == 0:
            print(f"{num} é par.")
            pares += 1
        else:
            print(f"{num} é ímpar.")
            impares += 1
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números inteiros ou 'fim'.")

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")

