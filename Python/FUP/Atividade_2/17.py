"""
Escreva uma função que, dadas as coordenadas x e y de pontos no R2
e retorne sua distância para a origem (0, 0)
"""
import math

def distancia_origem(x, y):
    distancia = math.sqrt(x**2 + y**2)
    return distancia

x = int(input("Digite a cordenada x: "))
y = int(input("Digite a cordenada y: "))
resultado = distancia_origem(x, y)
print(resultado)