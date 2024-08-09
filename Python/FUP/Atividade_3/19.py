"""
Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas
como pontos de exclamação, conforme o exemplo abaixo (para n = 5).
!
!!
!!!
!!!!
!!!!!
"""
def gerar(n):
    for i in range(1, n + 1):
        print("!" * i)

#exemplo de uso
n = int(input("Digite o numero de linhas desejado: "))
gerar(n)