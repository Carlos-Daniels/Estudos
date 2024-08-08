"""
Escreva uma função que receba n e k tais que k ≥ 0 e n ≥ k e calcule o coeficiente binomial
Cn,k = n!/(k!*(n-k)!)
"""
import math
def coeficiente_binomial(n,k):
    fatorial_n = math.factorial(n)
    fatorial_k = math.factorial(k)
    fatorial_nk = math.factorial(n - k)

    coef_binomial = fatorial_n / fatorial_k * fatorial_nk
    return coef_binomial

n = int(input("digite um valor inteiro para n (n >= k): "))
k = int(input("Digite um valor inteiro para k (k >= 0):"))

if k <0 or n <k:
    print ("Os valoes de n e k devem satisfazer n >= k e k >= 0")

else:
    resultado = coeficiente_binomial(n, k)
    print (f"O coeficiente binomial C ({n},{k}) é : {resultado}")