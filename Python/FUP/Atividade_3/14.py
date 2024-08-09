"""
Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da
série harmônica: H(n) = 1/1 + 1/2 + 1/3 … 1/n. Faça uma função que, dado um valor n
inteiro positivo, calcule o valor de H(n).
"""
def numero_harmonico(n):
    H_n = 0.0
    for i in range(1, n +1):
        H_n += 1/i
    return H_n

n = int(input("Digite um valor inteiro positivo n: "))
if n <= 0:
    print("O vakir de b deve ser um numero inteiro e positivo")
else:
    resultado = numero_harmonico(n)
    print(f"O numero harmonico H{n} é: {resultado}")