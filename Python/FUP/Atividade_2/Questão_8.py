"""
Faça uma função que converta a temperatura de graus Celsius para Fahrenheit. Fórmula: F =
C * (9.0/5.0) + 32
"""

def conversao(temp):
    return temp *(9.0/5.0) + 32
temp = float(input("Digite a Temperatura em graus Celcius: "))
fahrenheit = conversao(temp)

print(f"{temp}°C equivale a {fahrenheit}°F")