"""
Faça uma função que receba como parâmetro o ângulo x (em radianos) e um valor inteiro
positivo n . Calcule o valor do seno desse ângulo usando a respectiva série de Taylor: sin(x)
= x – x3
/3! + x5
/5! - … + (-1)n
(x2n+1)/(2n+1)!
"""
import math
def calcular_seno_taylor(x, n):
    soma = 0.0
    for i in range(n + 1):
        termo = ((-1)** i * x**(2*i + 1)) / math.factorial(2*i + 1)
        seno += termo
    return seno

#exemplo de uso
x = float(input("Digite o valor do angulo em radianos (x): "))
n = int(input("Digite o numero de termos da serie (n): "))
resultado = calcular_seno_taylor(x, n)
print(f"O valor aproximado do seno para x = {x} é: {resultado}")