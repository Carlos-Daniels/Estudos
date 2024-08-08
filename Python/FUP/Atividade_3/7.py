"""
Faça uma função que, dado número N, some todos os números inteiros de 1 a N, e retorne o
resultado obtido.
"""
def soma_inteiros(N):
    soma = 0
    for i in range(1, N + 1):
        soma += 1
    return soma 

#Exemplo de uso
N =  int(input("Digite um numero inteiro positivo N: "))
resultado = soma_inteiros(N)
print(f"A soma de todos os números inteiros de 1 até {N} é: {resultado}")