"""
Faça uma função que receba um valor inteiro n ≥ 0 e calcule o seu fatorial n!. Lembrete:
0! = 1
"""
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= 1  
    return resultado

n = int(input("Digite um valor inteiro n (n >= 0):"))

if n < 0:
    print ("O valor de n deve ser não negativo")

else :
    resultado = fatorial(n)
    print(f"O fatorial de {n} é : {resultado}")
    