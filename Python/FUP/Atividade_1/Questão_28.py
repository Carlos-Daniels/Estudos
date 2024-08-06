"""
Construa um programa que leia duas strings fornecidas pelo usuário e verifique se a segunda
string lida está contida no final da primeira, retornando o resultado da verificação.
"""

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

if primeira.endswith(segunda):
    print(f"A segunda string '{segunda}' esta contida no finalda primeira string '{primeira}'")

else: 
    print(f"A segunda string '{segunda}' não está contida no final da primeira string '{primeira}'")
