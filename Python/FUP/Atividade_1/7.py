'''
Faça um programa que leia a temperatura em graus Celsius e converta para Fahrenheit.
Fórmula: F = C * (9.0/5.0) + 32.
'''
celcius = float(input("qual a temperatura em celcius?"))
fahrenheit = celcius * (9.0/5.0) + 32

print(f"a temperatura {celcius}°C corresponde a {fahrenheit}°F")
