valor_saque = int(input("Digite o valor do saque: R$"))

notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
notas_1 = 0

if valor_saque >=100:
    notas_100 = valor_saque // 100
    valor_saque %= 100


if valor_saque >=50:
    notas_50 = valor_saque // 50
    valor_saque %= 50


if valor_saque >=20:
    notas_20 = valor_saque // 20
    valor_saque %= 20


if valor_saque >=10:
    notas_10 = valor_saque // 10
    valor_saque %= 10


if valor_saque >=5:
    notas_5 = valor_saque // 5
    valor_saque %= 5


if valor_saque >=2:
    notas_2 = valor_saque // 2
    valor_saque %= 2


if valor_saque >=1:
    notas_1 = valor_saque // 1
    valor_saque %= 1

print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 20: {notas_20}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 2: {notas_2}")
print(f"Notas de 1: {notas_1}")