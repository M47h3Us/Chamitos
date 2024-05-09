#Ex7
import random
print("Um orc misterioso apareceu, role um dado para matar esta vil criatura!!!")
menozum = 0
girada_de_dado = input("Deseja girar o dado? ")
if girada_de_dado == "sim":
    while menozum != "-1":
        numero_dado = random.randint(1, 20)
        if numero_dado == 1:
            print("Você errou o ataque!!!!")
        elif numero_dado >1 or numero_dado <=19:
            print(numero_dado)
        elif numero_dado == 20:
            print("ACERTO CRITICO!!!!")
        orc_se_ferro = input("Você possui vantagem contra o orc? ")
        if orc_se_ferro == "sim":
            dano_no_orc = int(input("Quanto de vantagem você tem contra o orc? "))
            coitado =  dano_no_orc + numero_dado
            print("você deu",coitado,"de dano no orc")
        elif orc_se_ferro == "não":
            print("Você deu", numero_dado , "de dano no orc")

        menozum = input("Caso deseje parar, digite -1: ")
else:
    print("Você fugiu do orc misterioso")
