"""
Faça uma função que receba um valor inteiro positivo em segundos, e retorne-o em horas,
minutos e segundos.
""" 
def converter (segundos):
    if segundos < 0:
        return "por favor, insira um valor inteiro positivo em segundos"
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    return horas, minutos, segundos_restantes

segundos = int(input("Digite um numero inteiro positivo em segundos: "))
resultado = converter(segundos)
print (f"{segundos} segundos equivalem {resultado} ")