"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada
do número. Se o número for negativo, mostre uma mensagem dizendo que o número é
inválido.
"""
import math
def calcular_raiz(num):
    if num >= 0:
        return math.sqrt(num)
    else:
        return "numero invalido, não é possivel calcular a raiz quadrada de um numero negativo"

num = float(input("Digite um numero: "))
resultado = calcular_raiz(num)
print (f"Resultado : {resultado}")
