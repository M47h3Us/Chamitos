print("Para parar o processo escreva parar ")
trava = 0
muita_coisa = 0
while trava != "para":
    numero = int(input("Coloque um numero: "))
    conta = input("Deseja fazer qual calculo? ")
    if conta == "+":
        muita_coisa = muita_coisa + numero
        print(muita_coisa)
    trava = input("Deseja parar? ")
    if trava == "parar":
        trava = "para"