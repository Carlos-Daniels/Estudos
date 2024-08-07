"""
 Crie uma função que, dado um ângulo em graus, retorne-o convertido em radianos. A
fórmula de conversão é: R = G * πR/180 , sendo G o ângulo em graus e R em radianos.
"""

import math

def conversao(graus):
    return graus * math.pi / 180

graus = float(input("Digite o valor em graus: "))
rad = conversao(graus)

print(f"{graus} graus equivalem a {rad: .2f} radianos")