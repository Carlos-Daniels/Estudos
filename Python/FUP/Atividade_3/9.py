"""
Faça uma função que calcule e retorne a soma dos N primeiros números pares (considere o 0
como o primeiro número par)
"""
def soma_pares(N):
    soma = 0
    for i in range(N):
        soma += 2 * i
    return soma
N = int(input("Digite um numero inteiro: "))
resultado = soma_pares(N)
print(f"A soma dos {N} primeiros numers pares é: {resultado}")