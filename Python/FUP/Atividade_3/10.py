"""
Faça uma função que receba um inteiro x e um inteiro não-negativo n e, usando laço de 
repetição, calcule x^n e retorne o resultado
"""
def potencia(x, n):
    resultado = 1 
    for i in range(n):
        resultado *= x
    return resultado

x = int(input("Digite um valor inteiro para x: "))
n = int(input("Digite um valor inteiro não-negativo para n: "))

if n < 0:
    print("o valor de n deve ser não-negativo")
else:
    resultado = potencia(x,n)
    print (f"O resultado de {x} elevado a {n} é : {resultado}")