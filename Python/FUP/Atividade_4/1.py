"""
Faça um programa que receba dois números inteiros e imprima o maior deles, se por acaso
os dois números forem iguais, imprima a mensagem “Numeros iguais”.
"""
def comparar(num1, num2):
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print("numeros iguais")

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
resultado = comparar(num1, num2)

if resultado == "numeros iguais":
    print(resultado)
else:
    print(f"O maior numero é : {resultado}")