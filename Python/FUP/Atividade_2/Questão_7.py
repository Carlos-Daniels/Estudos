"""
Faça uma função que, dado um número real, e retorne o resultado do quadrado desse
número
"""

def calcular(num):
    return num**2
num = float(input("Digite um numero real: "))
quadrado = calcular(num)

print(f"O quadrado de {num} é {quadrado}")