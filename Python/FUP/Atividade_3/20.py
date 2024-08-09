"""
Escreva uma função que gera um triângulo lateral de altura 2 × n − 1 e n de largura. Por
exemplo, a saída para n = 4 seria:
*
**
***
****
***
**
*
"""
def triangulo(n):
    #parte crescente do triangulo
    for i in range(1, n + 1):
        print("*" * 1)

    #parte decrescente do triangulo
    for i in range(n -1, 0, -1):
        print("*" * 1)

#exemplo de uso
n = int(input("Digite o valor de n: "))
triangulo(n)