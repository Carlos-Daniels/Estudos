"""
Crie uma função que permita fazer a conversão cambial de Dólares para Reais. Considere
como taxa de câmbio US$ 1,0 = R$5,27
"""

def cambio(dolar):
    return dolar / 5.27

dolar = float(input("Quantos dolares deseja cambiar para reais: "))
resultado = cambio(dolar)

print(f"Você tem {dolar} que equivalem á {resultado}")