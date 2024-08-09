"""
Faça um programa para exibir a tabuada de 1 a 9
"""
def tabuada():
    for i in range(1, 10):
        print (f"Tabuada de {i}")
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        print("-" * 15)
tabuada()