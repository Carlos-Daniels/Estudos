'''
Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via teclado,
calcule a área e o perímetro deste retângulo.
'''
base = float(input("qual o tamanho da base do retangulo? "))
altura = float(input("qual a altura do retangulo? "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"A area do retangulo é {area} e seu perimetro {perimetro}")
