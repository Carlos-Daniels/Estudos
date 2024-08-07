"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é:
R = G * π/180 , sendo G o ângulo em graus e R em radianos
"""
import math
ang_graus = float (input("Digite o angulo em graus: "))
ang_rad = ang_graus *math.pi / 180

print(f"o angulo {ang_graus}º corresponde a {ang_rad: .2f} radiandos")