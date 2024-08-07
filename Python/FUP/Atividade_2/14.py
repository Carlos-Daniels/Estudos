"""
Faça uma função que receba um número inteiro positivo de três dígitos (de 100 a 999).
Retorne outro número formado pelos dígitos invertidos do número lido. Exemplo: Entrada =
123, Saída = 321.
"""
def inverter_digitos(numeros):
    if 100 <= numeros <= 999:
        numero_invertido = int(str(numeros)[::-1])
        return numero_invertido
    else:
        return "Número fora do intervalo permitido"


numeros = int(input("Digite um numero de 3 digitos (100 a 999): "))
saida = inverter_digitos(numeros)
print(f"o numero {numeros} entra e sai {saida}")