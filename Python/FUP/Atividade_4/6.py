"""
Faça um programa que leia 3 notas, verifique se as notas são válidas e exiba na tela a média
destas notas com duas casas decimais. Uma nota válida deve ser, obrigatoriamente, um valor
entre 0.00 e 10.00, onde caso a nota não possua valor válido, este fato deve ser informado ao
usuário e o programa termina.
"""
def ler():
    nota = float(input("Digite uma nota (entre 0.00  e 10.00): "))
    if 0.00 <= nota <10.00:
        return nota
    else:
        print("Nota invalida. o programa sera encerrado")
        return None
    
def cal_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

n1 = ler()
if n1 is None:
    exit()
n2 = ler()
if n2 is None:
    exit
n3 = ler()
if n3 is None:
    exit()

media = cal_media(n1, n2, n3)
print(f"A media das notas é: {media:.2f}")