"""
Leia uma string contendo letras de uma frase, inclusive os espaços em branco. Retirar os
espaços em branco e depois escrever a frase resultante.
"""
frase = input("Digite uma frase:")
frase_sem_espaços = frase.replace(" " , "")

print(f" A frase sem espaçoes é: {frase_sem_espaços}")
