import math

x = float(input("Digite a cordenada x do ponto:"))
y = float(input("Digite a cordenada y do ponto:"))

distancia = math.sqrt(x**2 + y**2)

print(f"A distancia do ponto({x}, {y})a origem (0, 0) é {distancia: .2f}")