"""
Crie uma função que, dados três valores, retorne a soma dos quadrados dos três valores e o
quadrado da soma dos três valores
"""

def calcular(val1, val2, val3):
    soma = val1**2 + val2**2 + val3**2
    quadrado = (val1 + val2 + val3)**2
    return soma, quadrado
val1 = float(input("Digite um valor: "))
val2 = float(input("Digite mais um valor: "))
val3 = float(input("Digite um ultimo valor:"))

soma, quadrado = calcular(val1, val2, val3)
print(f"A soma dos quadrados dos valores é: {soma}")
print(f"O quadrado da soma dos valores é: {quadrado}")