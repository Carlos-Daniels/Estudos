"""
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere
outro número formado pelos dígitos invertidos do número lido. Exemplo: Número Lido =
123, Número Gerado = 321
"""
numero = int(input("digite um numero inteiro de 3 digitos( de 100 a 999): "))

if 100 <= numero <= 999:
    numero_invertido = int(str(numero)[::-1])

    print(f"numero lido = {numero}, numero gerado = {numero_invertido}")
else:
    print("numero invalido, por favor digite um numero inteiro de 3 digitos (de 100 a 999)")