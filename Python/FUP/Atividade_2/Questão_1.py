"""
Crie uma função que receba como parâmetro um número inteiro e devolva o seu dobro
"""
def dobro(num):
    return num * 2

num = int(input("Digite um numero inteiro: "))
resultado = dobro(num)

print(f"o dobro de {num} é {resultado}")