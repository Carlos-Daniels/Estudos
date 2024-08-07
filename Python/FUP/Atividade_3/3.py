"""
Faça um programa que peça ao usuário para digitar 10 valores e mostre a soma deles
"""
soma = 0 
for i in range(10):
    valor = float(input(f"digite o valor {i+1}: "))
    soma += valor

print(f" A soma dos valores digitados é: {soma}")