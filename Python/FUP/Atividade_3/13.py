"""
O número de Fibonacci Fn para n > 0 é definido da seguinte maneira:
◦ F1 = 1
◦ F2 = 1
◦ Fn = Fn−1 + Fn−2 para n> 2
"""

def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    fib1, fib2 = 1, 1

    for i in range(3, n + 1):
        fibn = fib1 +fib2 #fn = fn-1 + fn-2
        fib1, fib2 = fib2, fibn

    return fibn

n = int(input("Digite um valor inteiro n (n > 0): "))

if n < 0:
    print("O valor de n deve ser maior que 0")
else:
    resultado = fibonacci(n)
    print(f"O numero de fibonacci F{n} é : {resultado}")
    