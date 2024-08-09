"""
Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da
palavra. Imprima a string resultante.
"""
def incrementar(palavra):
    resultado = ""
    for char in palavra:
        novo_char = chr(ord(char) + 1)
        resultado += novo_char
    return resultado

#exemplo de uso

palavra = input("Digite uma palavra: ")
incrementada = incrementar(palavra)
print(f"A palavra com ASCII incrementado é: {incrementada}")