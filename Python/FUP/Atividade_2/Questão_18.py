"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
proporcionalmente ao valor que cada deu para a realização da aposta. Faça uma função que
receba quanto cada apostador investiu e o valor do prêmio, e retorne quanto cada um
ganharia do prêmio com base no valor investido.
"""

def calcular (ap1, ap2, ap3, premio):
    total = ap1 + ap2 + ap3
    pre1 = (ap1 / total) * premio
    pre2 = (ap2 / total) * premio
    pre3 = (ap3 / total) * premio
    return pre1, pre2, pre3

# exemplo de uso
ap1 = 100
ap2 = 200
ap3 = 300
premio = 6000

pre1, pre2, pre3 = calcular(ap1, ap2, ap3, premio)
print(f"Amigo 1 ganhará: R${pre1:.2f}")
print(f"Amigo 2 ganhará: R${pre2:.2f}")
print(f"Amigo 3 ganhará: R${pre3:.2f}")