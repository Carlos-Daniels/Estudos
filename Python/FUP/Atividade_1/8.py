'''
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6 , sendo K a velocidade em km/h
e M em m/s.
'''
km = float(input("qual a velocidade em KM/h? "))
ms = km / 3.6

print(f" a velocidade do objeto que estava a {km: .2f}KM/h em metros por segundo é {ms: .2f}")