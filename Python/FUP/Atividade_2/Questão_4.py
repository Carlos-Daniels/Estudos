"""
Faça uma função que, dado um número inteiro e retorne o seu antecessor e o seu sucessor
"""
def antecessor_sucessor(num):
    antecessor = num - 1
    sucessor = num + 1
    return(antecessor, sucessor)

num = int(input("Digite um numero inteiro: "))

antecessor, sucessor = antecessor_sucessor(num)

print(f"O antecessor de {num} é {antecessor} e sucessor é {sucessor}")