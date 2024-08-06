"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganharia do prêmio com base no valor investido.
"""

invest1 = float(input("digite o valor investido pelo primeiro apostador:"))
invest2 = float(input("Digite o valor investido pelo segundo apostador: "))
invest3 = float(input("Digite o valor investido pelo terceiro apostador: "))

valor_premio = float(input("digite o valor do premio: R$"))

total_invest = invest1 + invest2 + invest3

ganho1 = (invest1 / total_invest) * valor_premio
ganho2 = (invest2 / total_invest) * valor_premio
ganho3 = (invest3 / total_invest) * valor_premio

print(f"O primeiro apostador ganharia R${ganho1:.2f}, o segundo R${ganho2: .2f} e o terceiro R${ganho3: .2f}")