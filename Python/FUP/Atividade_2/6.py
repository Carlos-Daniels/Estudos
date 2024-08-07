"""
 Elabore uma função para calcular o volume (V) de uma esfera e a área (A) de sua superfície,
dado o valor de seu raio (R). A fórmula do volume da esfera é V = 4/3 πRR3
 e A = 4πRR2
"""
import math

def calcular(raio):
    volume = 4/3 * math.pi * raio**3
    area = 4* math.pi * raio**2
    return volume, area

raio = float(input("Digite valor do raio da esfera em cm: "))
volume, area = calcular(raio)

print(f"Uma esfera de raio {raio}cm tem {volume: .2f}cm cubicos de volume e {area: .2f}cm quadrados de areas")