"""
Faça um programa que calcule e escreva o valor de
S = 1/1 + 3/2 + 5/3 + 7/4 + … + 99/50.
"""
def calcular():
    S = 0.0
    numerador = 1

    for denominador in range (1,51):
        S += numerador / denominador
        numerador += 2
    return S

#exemplo de uso
resultado = calcular()
print(f"O valor de S é: {resultado: .2f}")