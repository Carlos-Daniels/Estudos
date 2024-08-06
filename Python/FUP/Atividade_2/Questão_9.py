"""
Crie uma função que, dada uma velocidade em km/h (quilômetros por hora) e retorne-a
convertida em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6 , sendo K a
velocidade em km/h e M em m/s.
"""

def conversao(kmh):
    return kmh/3.6

kmh = float(input("Digite a velocidade em KM/h: "))
ms = conversao(kmh)

print(f"{kmh}KM/h equivalem a {ms: .2f}m/s")