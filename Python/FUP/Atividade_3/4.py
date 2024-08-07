"""
Faça um programa que leia 10 inteiros e imprima sua média
"""
soma = 0
for i in range(10):
    valor =  int(input(f"Digite o valor inteiro {i+1}"))
    soma += valor

media = soma /10
print(f"A media dos valores digitados é : {media}")
