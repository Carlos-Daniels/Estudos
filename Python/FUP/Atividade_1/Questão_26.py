"""
Faça um programa em que troque todas as ocorrências de uma letra L1 pela letra L2 em uma
string. A string e as letras L1 e L2 devem ser fornecidas pelo usuário
"""

string = input("Digite uma string: ")

L1 = input("Digite a letra a ser substituida: ")
L2 = input("Digite a letra substituta: ")

nova_str = string.replace(L1,L2)

print(f"A nova string após substituir '{L1}' por '{L2}' é : {nova_str}")