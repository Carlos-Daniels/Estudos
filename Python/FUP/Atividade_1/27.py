"""
Escreva um programa que recebe do usuário uma string S, um caractere C, e uma posição I e
devolve o índice da primeira posição da string onde foi encontrado o caractere C. A procura
deve começar a partir da posição I.
"""
S = input("Digite uma string S: ")
C = input("Digite um caractere C: ")
I = int(input("Digite a posição inicial I (indice)"))

indice = S.find(C,I)

if indice != -1:
    print(f"A primeira posição de  '{C}' em '{S}' a partir da posição {I} é :{indice}")

else:
    print(f"O caractere '{C}' não foi encontrado em '{S}' a partir da posição {I}")