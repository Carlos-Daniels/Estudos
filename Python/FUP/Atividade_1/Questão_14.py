"""
 Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
"""

numero = int(input("Digite um numero intero de 4 digitos (de 1000 a 9999):"))

if 1000 <= numero <= 9999:
    numero_str = str(numero)

    for digito in numero_str:
        print(digito)

else:
    print("Numero digitado invalido, por favor, digite um numero inteiro de 4 digitos (de 1000 a 9999)")