"""
Faça um programa que desenhe uma linha na tela usando vários símbolos de igual (Ex:
========). O programa deve ler quantos sinais de iguais serão mostrados.
"""
def desenhar(n):
    linha = "=" * n
    print (linha)

#exemplo de uso
n = int(input("Digite a quantidade de sinais de igual você quer: "))
desenhar(n)
