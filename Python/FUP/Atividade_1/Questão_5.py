'''
Elaborar um programa para calcular e imprimir o volume (V) de uma esfera e a área (A) de
sua superfície, dado o valor de seu raio (R). A fórmula do volume da esfera é V = 4/3 πR3 e
A = 4πR2
'''
import math

raio = float(input("digite o raio da esfera em cm: "))

volume = (4/3) * math.pi * raio**3
area = 4 * math.pi * raio**2

print(f"uma esfera de raio {raio}cm tem {volume: .2f}cm cubicos de volume e uma area de {area: .2f}cm quadrados ")