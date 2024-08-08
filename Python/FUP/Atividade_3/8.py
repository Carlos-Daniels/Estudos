"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros números
naturais ímpares.
"""
n = int(input("Digite um numero inteiro: "))
count = 0
num = 1

while count < n:
    if  num % 2 != 0:
        print(num)
        count += 1
    num += 1