"""
Faça um programa que receba um número inteiro e imprima se o número é par ou ímpar
"""
def impar_par(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"
    
#exemplo de uso
num = int(input("Digite um numero inteiro: "))
resultado = impar_par(num)
print(f"O numero {num} é {resultado}")