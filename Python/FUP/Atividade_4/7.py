"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação
for maior que 20% do salário então imprima: "Emprestimo nao concedido", caso contrário
imprima: "Emprestimo concedido"
"""
salario = float(input("Digite o salario do trabalhador: "))
prestacao = float(input("Digite o valor da prestação do emprestimo: "))

limite = 0.2 * salario

if prestacao > limite: 
    print("Salario não concedido")
else:
    print("Emprestimo concedido")
    