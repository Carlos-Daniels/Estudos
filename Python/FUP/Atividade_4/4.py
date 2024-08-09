"""
Ler três valores e determinar o maior entre eles
"""
def comparar(x, y, z):
    maior = x
    if y > maior:
        maior = y
    if z > maior:
        maior = z
    return maior

x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))
z = float(input("Digite o terceiro valor: "))

maior = comparar(x, y, z)
print(f"O maior valor é : {maior}")