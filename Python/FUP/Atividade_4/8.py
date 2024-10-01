"""
Faça um programa que receba dois números e execute as operações listadas a seguir de
acordo com a escolha do usuário:
◦ 1: Média entre os números digitados
◦ 2: Diferença do maior pelo menor
◦ 3: Produto entre os números digitados
◦ 4: Divisão do primeiro pelo segundo
"""
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

print("\nEscolha uma das operações:")
print("1: media entre os dois numeros digitados")
print("2: diferença do maior pelo menor")
print("3: Produto entre os numeros digitados")
print("4: Divisão do primeiro pelo segundo")

escolha = int(input("\nDigite a operação desejada (1 - 4): "))

if escolha == 1:
    media = (n1 + n2) / 2
    print(f"A media entre os numeros é : {media}")
elif escolha == 2:
    diferença = abs(n1 -n2)
    print (f"A diferença do maior pelo maior é : {diferença}")
elif escolha == 3: 
    produto = n1 * n2
    print(f"O produto entre os numeros é : {produto}")
elif escolha == 4: 
    if n1 != 0:
        diviso = n1 / n2
        print(f"A divisão do primeiro pelo segundo: {diviso}")
    else: 
        print("erro: divisão por zero não é permitida.")

else:
    print("Operação invalida. Por favor, escolha um numero entre 1 e 4.")