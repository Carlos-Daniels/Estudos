"""
Faça uma função que receba um número inteiro de 4 dígitos (de 1000 a 9999) e retorne os 4
dígitos separados, cada um em uma variável diferente.
"""

def separar_digitos(numero):
    if 1000 <= numero <= 9999:
        d1 = int(str(numero)[0])
        d2 = int(str(numero)[1])
        d3 = int(str(numero)[2])
        d4 = int(str(numero)[3])
        return d1, d2, d3, d4
    else:
        return "Numero invalido"
    
numero = int(input("Digite um numero de 4 digitos"))
d1, d2, d3, d4 = separar_digitos(numero)
print(f"numero = {numero}, digitos separados: {d1}, {d2}, {d3}, {d4}.")