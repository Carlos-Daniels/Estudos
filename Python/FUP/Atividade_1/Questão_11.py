"""
Faça um programa que receba o salário de um funcionário. Calcule e imprima o valor do
novo salário, sabendo que ele recebeu um aumento de 21,37 %
"""

salario = float(input("qual o valor do salario do funcionario? "))
aumento = salario * 21.37 / 100
nv_salario = salario + aumento
print(f"O funcionario em questão que tinha um salario de {salario} recebeu um aumento de {aumento} passando a receber {nv_salario}")