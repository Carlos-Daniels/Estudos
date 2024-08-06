"""
Faça uma função que, a partir das medidas dos lados de um retângulo, calcule a área e o
perímetro deste retângulo.
"""
def calculo(lado1, lado2):
    area = lado1 * lado2
    perimetro = 2 * (lado1 + lado2)
    return area, perimetro

lado1 = float(input("Qual a medida em cm da largura do retangulo: "))
lado2 = float(input("Qual a medida em cm da altura do retangulo: "))

area, perimetro = calculo(lado1, lado2)

print(f"O retangulo com {lado1}cm de largura e {lado2}cm de altura tem {area}cm de area e {perimetro}cm de perimetro.")