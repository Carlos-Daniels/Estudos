"""
 Faça um programa que receba um valor em R$ que será dividido entre três ganhadores de
um concurso. Sendo que da quantia total:
◦ O primeiro ganhador receberá 46%;
◦ O segundo ganhador receberá 32%;
◦ O terceiro receberá o restante;
"""
valor_total = float(input("Digite o valor total do premio em: R$ "))
primeiro = valor_total * 0.46
segundo = valor_total * 0.32
terceiro = valor_total - (primeiro + segundo)

print(f"Do premio de R${valor_total} o primeiro ganhador vai receber R${primeiro}, o segundo R${segundo}, e, o terceiro{terceiro}")