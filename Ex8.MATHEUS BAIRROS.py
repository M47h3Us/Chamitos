#Ex8
email = input("Porfavor ensira seu email: ")
usuario = input("Porfavor ensira o nome de usuario: ")
senha = int(input("Porfavor ensira a senha de usuario: "))
confirmar_senha = int(input("Porfavor reensira a senha: "))
if confirmar_senha != senha:
    print("Senhas não compativeis")
    while confirmar_senha != senha:
        senha = int(input("Porfavor ensira a senha de usuario: "))
        confirmar_senha = int(input("Porfavor reensira a senha: "))
        if confirmar_senha != senha:
            print("Senhas não compativeis")
login = print("Bem vindo ao site! Porfavor ensira as informações da conta: ")
confirmar_email = input("Porfavor ensira seu email: ")
if confirmar_email != email:
    print("Emails não compativeis")
    while confirmar_email != email:
        confirmar_email = input("Porfavor ensira seu email: ")
        if confirmar_email != email:
            print("Senhas não compativeis")
confirmar_usuario = input("Porfavor ensira o nome de usuario: ")
if confirmar_usuario != usuario:
    print("Usuarios não compativeis")
    while confirmar_usuario != usuario:
        confirmar_usuario = input("Porfavor ensira seu usuario: ")
        if confirmar_usuario != usuario:
            print("Usuarios não compativeis")
confirmar_senhas = int(input("Porfavor ensira a senha de usuario: "))
if confirmar_senhas != senha:
    print("Senhas não compativeis")
    while confirmar_senhas != senha:
        confirmar_senhas = int(input("Porfavor ensira a senha de usuario: "))
        if confirmar_senhas != senha:
            print("Senha não reconhecida")
if confirmar_email == email and confirmar_usuario and confirmar_senhas == senha:
    print("Cadastro feito com sucesso!")