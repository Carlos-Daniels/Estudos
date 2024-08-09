"""
Faça uma função que receba um inteiro n como parâmetro, calcule e retorne o resultado da
seguinte série: S = 2/4 + 5/5 + 10/6 + … + (n2
 + 1)/(n + 3)
"""
def calcular(n):
    soma = 0.0
    for k in range(1, n + 1 ):
        termo =  (k ** 2 + 1) / (k + 3)
        soma += termo
    return soma

#exemplo de uso
n = int(input("Digite o valor de n: "))
resultado = calcular(n)
print(f"O resultado da serie para n = {n} é {resultado:.4f}")