"""
Faça um programa que receba uma palavra e a imprima de trás-para-frente
"""
def inverter(palavra):
    return(palavra[::-1])

#exemplo de uso
palavra = input("Digite uma palavra: ")
inverter_palavra =inverter(palavra)
print(f"A palavra invertida é: {inverter_palavra}")