'''Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.'''

import random
import string

tamanho = int(input("Quantidade de caracteres para a senha: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
print(f"Senha gerada: {senha}")
