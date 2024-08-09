"""
Faça uma função que, dado um valor N inteiro e positivo, calcule o valor de E, conforme a
fórmula a seguir: E = 1 + 1/1! + 1/2! + 1/3! … 1/n!
"""

import math
def calcular_E(N):
    E = 1.0
    for i in range(1, N + 1):
        E += 1 / math.factorial(1)
    return E

#exemplo de uso
N = 5
resultado = calcular_E(N)
print(f"O valor de E para N = {N} é: {resultado}")