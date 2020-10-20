from math import (cos, sin, tan, atan, pi, sqrt)
from math import degrees as deg, radians as rad

d = float(input("Profundidade da ferramenta (m): "))
w = float(input("Largura da ferramenta (m): "))

# Primeiro passo: Tipo de ferramenta

if d/w < 1:
  dc = d
  print("----------------------------------------------")
  print("d/w = {:.3f}".format(d/w))
  print("Tipo de ferramenta: Blade (larga => d/w < 1)")
  print("dc = d = {:.3f} m".format(dc))
  print("----------------------------------------------")
elif (d/w >= 1 and d/w < 6):
  dc = d
  print("---------------------------------------------------------")
  print("d/w = {:.3f}".format(d/w))
  print("Tipo de ferramenta: Narrow tine (Estreita => 1 < d/w < 6)")
  print("dc = d = {:.3f} m".format(dc))
  print("---------------------------------------------------------")
else:
  dc = w + .6 * d
  print("----------------------------------------------------------------")
  print("d/w = {:.3f}".format(d/w))
  print("Tipo de ferramenta: Very narrow tine (Muito estreita => d/w > 6)")
  print("dc = w + 0.6 * d = {:.3f} m".format(dc))
  print("----------------------------------------------------------------")

# Segundo passo: Acha o valor de beta crítico
alpha = float(input("Ângulo de ataque (alpha, em graus): "))
m = 4.0704 - (0.0940983 * alpha) + (0.00149667 * alpha**2) - (0.0000121924 * alpha**3) + (3.963 * 10**(-8) * alpha**4)

beta = deg(atan(1/(m - (tan(rad(alpha)))**(-1))))

print("---------------------------------------------")
print("alpha = {:.2f} => m = {:.2f}".format(alpha, m))
print("beta crítico = {:.2f}°".format(beta))
print("---------------------------------------------")

# Terceiro passo: Obter os adimensionais

print("Cálculo dos adimensionais")
print("---------------------------------------------")

delta = float(input("Valor de delta (em graus): "))
phi = float(input("Valor de phi (em graus): "))
b = float(input(("Valor de b (em metros): ")))
rho = float(input("Valor de rho (em graus): "))
r = d * ((tan(rad(alpha)))**(-1) + (tan(rad(beta)))**(-1))

ngamma = (r/(2*d) * (1 + (2 * r)/(3 * b) * sin(rad(rho))))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * (tan(rad(beta + phi)))**(-1))
nq = ((r/d) * (1 + (r/b) * sin(rad(rho))))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * (tan(rad(beta + phi)))**(-1))
nca = (1 - (tan(rad(alpha)))**(-1) * (tan(rad(beta + phi)))**(-1))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * (tan(rad(beta + phi)))**(-1))
nc = (1 + tan(rad(beta))**(-1) * tan(rad(beta + phi))**(-1) * (1 + (r/b) * sin(rad(rho))))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * tan(rad(beta + phi))**(-1))
na = (tan(rad(beta)) + (tan(rad(beta + phi)))**(-1))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * (tan(rad(beta + phi)))**(-1))

print("-------------------------------------------------")
print("ngamma = {:.2f}".format(ngamma))
print("nq = {:.2f}".format(nq))
print("nca = {:.2f}".format(nca))
print("nc = {:.2f}".format(nc))
print("-------------------------------------------------")

q = float(input("Valor do carregamento (q, em Pascal): "))
c = float(input("Valor de c (em Pa): "))
ca = float(input("Valor de ca (em Pa): "))
gamma = float(input("Peso específico (gamma, em N/m³): "))

print("-------------------------------------------------")
v = float(input("Velocidade de operação (km/h): "))
v /= 3.6
print("-------------------------------------------------")

vc = sqrt(5 * 9.81 * dc) # velocidade crítica 

if v <= vc:
  h = (gamma * dc**(2) * ngamma + c * dc * nc + q * dc * nq) * (w + dc * (m - (m - 1)/3)) * sin(rad(alpha + delta))
  vn = -((gamma * dc**(2) * ngamma + c * dc * nc + q * d * nq) * (w + dc * (m - (m - 1)/3))) * cos(rad(alpha + delta))
  print("v <= vc = {:.2f} km/h, logo v não influencia na força horizontal (H) requerida".format(vc * 3.6))
else:
  h = ((gamma * dc**(2) * ngamma + c * dc * nc + q * dc * nq) * (w + dc * (m - (m - 1)/3)) + (gamma * v**(2) * na * dc * (w + .6 * d)/9.81)) * sin(rad(alpha + delta))
  vn = -((gamma * dc**(2) * ngamma + c * dc * nc + q * dc * nq) * (w + dc * (m - (m - 1)/3)) + (gamma * v**(2) * na * dc * (w + .6 * d)/9.81)) * cos(rad(alpha + delta))
  print("v > vc = {:.2f} km/h, logo v influencia na força horizontal (H) requerida".format(vc * 3.6))

print("H = {:.2f} N".format(h))
print("V = {:.2f} N".format(vn))
print("-------------------------------------------------")
