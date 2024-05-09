#Ex2
print("Exemplo: 2(numero) 3(expoente)")
calculo = input("Coloque a base e o expoente: ")
calculo = calculo.split(" ")
base = int(calculo[0])
expoente = int(calculo[1])
resultado = base ** expoente
print(resultado)