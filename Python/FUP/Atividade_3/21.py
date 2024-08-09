"""
Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1 . Por exemplo, a
saída para n = 6 seria:
*
***
*****
*******
*********
***********
"""
def gerar(n):
    for i in range(1, n + 1):
        num_asteriscos = 2 * i - 1
        print("*" * num_asteriscos)

#exemplo de uso
n = int(input("Digite a altura do triangulo n: "))
gerar(n)