"""
Escreva uma função que receba como entrada o valor do saque realizado pelo cliente de um
banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a
menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real
"""

def calcular(saque):
    notas = [100, 50, 20, 10, 5, 2, 1]
    quantidade = {}

    #calcula a quantidade necessaria de cada nota
    for nota in notas:
        quantidade[nota] = saque // nota
        saque %= nota
    
    return quantidade

#exemplo de uso
valor_saque = 387
resultado = calcular(valor_saque)
print(f"Para o saque de R${valor_saque}, serão necessárias:")
for nota, quantidade in resultado.items():
    print(f"{quantidade} nota(s) de R${nota}")