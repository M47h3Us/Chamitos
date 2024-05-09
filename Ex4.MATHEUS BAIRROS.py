#Ex4
print("As formas de escrever as bandeiras são: Verde, Amarela, Vermelha ")
falido = int(input("Coloque o valor da conta: "))
bandera = input("Coloque a bandeira: ")

if bandera == "Verde":
    resultado = falido * 1
    print(resultado)
elif bandera == "Amarela":
    resultado = falido * 3
    print(resultado)
elif bandera == "Vermelha":
    resultado = falido * 7
    print(resultado)