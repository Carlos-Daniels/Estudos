"""
Ler 4 números inteiros e calcular a soma dos que forem par
"""
def soma_pares(*numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    return soma