"""
Faça uma função que receba um valor em R$ que será dividido entre três ganhadores de um
concurso. Sendo que da quantia total:
◦ O primeiro ganhador receberá 46%;
◦ O segundo ganhador receberá 32%;
◦ O terceiro receberá o restante;
"""

def divisao(total):
    primeiro = total * 0.46
    segundo = total *0.32
    terceiro = total * (1 - 0.46 - 0.32)
    return primeiro, segundo, terceiro

total = float(input("Digite o valor total do premio R$"))
primeiro, segundo, terceiro = divisao(total) 