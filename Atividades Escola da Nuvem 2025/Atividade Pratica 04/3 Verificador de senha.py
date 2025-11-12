'''Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.'''

while True:
    senha = input("Digite uma senha forte (mínimo 8 caracteres e pelo menos um número), ou 'sair' para encerrar: ")
    if senha.lower() == 'sair':
        print("Operação encerrada.")
        break
    if len(senha) < 8:
        print("Senha fraca: precisa de pelo menos 8 caracteres.")
        continue
    if not any(char.isdigit() for char in senha):
        print("Senha fraca: precisa conter ao menos um número.")
        continue
    print("Senha considerada forte!")
    break
