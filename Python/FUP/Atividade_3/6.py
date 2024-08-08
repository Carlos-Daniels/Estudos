"""
Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e
mostre o resultado obtido
"""
N = int(input("Digite um numero positivo N: "))
soma = 0

for i in range(1, N + 1):
    soma += i
print (f"A soma de todos os numeros inteiros de 1 até {N} é: {soma}")