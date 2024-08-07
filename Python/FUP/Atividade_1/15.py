"""
Leia um valor inteiro positivo em segundos, e imprima-o em horas, minutos e segundos
"""

segundos_totais = int(input("Digite um valor positivo em segundos:"))

if segundos_totais >= 0:
    horas = segundos_totais // 3600
    minutos = (segundos_totais % 3600)  // 60
    segundos = segundos_totais % 60

    print(f"{segundos_totais} segundos equivalem a {horas} horas, {minutos} minutos e {segundos} segundos.")
else:
    print("Valor inválido! Por favor, digite um valor inteiro positivo.")