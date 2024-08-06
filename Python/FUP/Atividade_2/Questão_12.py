"""
Faça uma função que receba o salário de um funcionário e calcule o valor do novo salário,
sabendo que ele recebeu um aumento de 21,37 %.
"""
def alteração(salario):
    return salario * 0.2137
salario = float(input("Digire o valor do salario do funcionario: "))
novo = alteração(salario) + salario

print(f"O novo salario é de R${novo: .2f}")