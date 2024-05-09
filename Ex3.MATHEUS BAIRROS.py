#Ex3
import random
para = 0
while para != "parar":
    numero_aleatorio = random.randint(1,3)
    print(numero_aleatorio)
    if numero_aleatorio == 1:
        print("Não foi dessa vez")
    elif numero_aleatorio == 2:
        print("Nossa foi quase!")
    elif numero_aleatorio == 3:
        print("Passou raspando!!!")
    rerolar = input("Deseja continuar ou parar? ")
    if rerolar == "parar":
        para = "parar"
    else:
        para = "pão de queijo"