from math import (cos, sin, tan, atan, pi)
from math import degrees as deg, radians as rad

d = float(input("Profundide da ferramenta (m): "))
w = float(input("Largura da ferramenta (m): "))
delta = float(input("Valor de delta (em graus): "))
phi = float(input("Valor de phi (em graus): "))
c = float(input("Valor de c (em Pa): "))
ca = float(input("Valor de ca (em Pa): "))
gamma = float(input("Peso específico (gamma, em N/m³): "))

# Primeiro passo: Tipo de ferramenta

if d/w < 1:
  print("Blade")
  dc = d
elif (d/w >= 1 and d/w < 6):
  print("Narrow tine")
  dc = d
else:
  print("Very narrow tine")
  dc = d

# Segundo passo: Acha o valor de beta crítico
alpha = float(input("Ângulo de ataque (alpha, em graus): "))
m = 4.0704 - (0.0940983 * alpha) + (0.00149667 * alpha**2) - (0.0000121924 * alpha**3) + (3.963 * 10**(-8) * alpha**4)

beta = deg(atan(1/(m - (tan(rad(alpha)))**(-1))))

# Terceiro passo: Obter os adimensionais

r = d * ((tan(rad(alpha)))**(-1) + (tan(rad(beta)))**(-1))
b = float(input(("Valor de b (em metros): ")))
rho = float(input("Valor de rho (em graus): "))

ngamma = (r/(2*d) * (1 + (2 * r)/(3 * b) * sin(rad(rho))))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * (tan(rad(beta + phi)))**(-1))

nc = (1 + tan(rad(beta))**(-1) * tan(rad(beta + phi))**(-1) * (1 + (r/b) * sin(rad(rho))))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * tan(rad(beta + phi))**(-1))

q = float(input("Valor do carregamento (q, em Pascal): "))

h = (gamma * dc**(2) * ngamma + c * dc * nc + q * dc * 0) * (w + d * (m - (m - 1)/3)) * sin(rad(alpha + delta))

print(m, beta, r, ngamma, nc, h)