"""
Faça uma função que receba um número inteiro positivo P e retorne a soma dos algarismos
de P! . Exemplo: Se P = 4 , P! = 24 . Logo, a soma de seus algarismos é 2 + 4 = 6.
"""

import math
def soma_fatorial(P):
    fatorial = math.factorial(P)
    fatorial_str = str(fatorial)
    soma = sum(int(digito) for digito in fatorial_str)
    return soma

#exemplo de uso
P = 4
resultado = soma_fatorial(P)
print(f"A soma dos algarismos de {P} é: {resultado}")