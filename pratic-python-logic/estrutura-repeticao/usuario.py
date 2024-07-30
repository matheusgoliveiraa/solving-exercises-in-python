# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informaçõe

while True:
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite a sua senha: ")

    if usuario != senha:
        print(f"{usuario} login efetuado, com sucesso!")
        break

    else:
        print("Senha igual ao nome de usuário, favor mudar a senha.")