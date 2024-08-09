"""
Implemente um programa que leia duas strings, str1 e str2, e um valor inteiro positivo N.
Concatene N vezes a string str2 ao final da string str1
"""
def concatenar(str1, str2,n):
    return str1 + (str2 * n)

#exemplo de uso
str1 = input("Digite a primeira string (str1): ")
str2 = input("Digite a segunda string (str2): ")
n = int(input("Digite um valor inteiro positivo N: "))

if n >= 0:
    resultado = concatenar(str1, str2, n)
    print(f"Resultado da cocatenação: {resultado}")
else:
    print("O valor de N deve ser um numero inteiro positivo")
