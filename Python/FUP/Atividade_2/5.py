"""
Faça uma função que, dado o tamanho do lado de um quadrado e retorne a sua área
"""
def calculo(lado):
    area = lado * lado
    return area
lado = float(input("Digite a medida do lado do quadrado em cm: "))
area = calculo(lado)


print(f"O quadrado de medida {lado}cm tem uma area de {area: .2f}cm quadrados")