"""
Faça um programa que leia um inteiro n ≥ 0 . Escreva n vezes a seguinte mensagem: “Estou
sabendo Programar haha”
"""
def imprimir_n_vezes(n):
    mensagem = "Estou sabendo programar haha"
    for _ in range(n):
        print(mensagem)

#exemplo de uso
n = int(input("Digite um numero inteiro n ≥ 0: "))
if n >= 0:
    imprimir_n_vezes
else :
    print("O numero deve ser maior ou igual a 0.")
