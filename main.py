from math import (cos, sin, tan, atan, pi, sqrt)
from math import degrees as deg, radians as rad

d = float(input("Profundidade da ferramenta (m): "))
w = float(input("Largura da ferramenta (m): "))

# Primeiro passo: Tipo de ferramenta

if d/w < 1:
  dc = d
  print("----------------------------------------------")
  print("d/w = {:.4f}".format(d/w))
  print("Tipo de ferramenta: Blade (larga => d/w < 1)")
  print("dc = d = {:.4f} m".format(dc))
  print("----------------------------------------------")
elif (d/w >= 1 and d/w < 6):
  dc = d
  print("---------------------------------------------------------")
  print("d/w = {:.4f}".format(d/w))
  print("Tipo de ferramenta: Narrow tine (Estreita => 1 < d/w < 6)")
  print("dc = d = {:.4f} m".format(dc))
  print("---------------------------------------------------------")
else:
  dc = w + .6 * d
  print("----------------------------------------------------------------")
  print("d/w = {:.4f}".format(d/w))
  print("Tipo de ferramenta: Very narrow tine (Muito estreita => d/w > 6)")
  print("dc = w + 0.6 * d = {:.4f} m".format(dc))
  print("----------------------------------------------------------------")

# Segundo passo: Acha o valor de beta crítico

alpha = float(input("Ângulo de ataque (alpha, em graus): "))

question = input("Beta crítico é dado? [S]im ou [N]ão: ")

if question == "S":
  beta = float(input("Valor de beta em graus: "))
  m = 4.0704 - (0.0940983 * alpha) + (0.00149667 * alpha**2) - (0.0000121924 * alpha**3) + (3.963 * 10**(-8) * alpha**4)
else:
  m = 4.0704 - (0.0940983 * alpha) + (0.00149667 * alpha**2) - (0.0000121924 * alpha**3) + (3.963 * 10**(-8) * alpha**4)
  beta = deg(atan(1/(m - (tan(rad(alpha)))**(-1))))

r = dc * ((tan(rad(alpha)))**(-1) + (tan(rad(beta)))**(-1))

print("---------------------------------------------")
# print("alpha = {:.4f}° => m = {:.4f}".format(alpha, m))
print("beta crítico = {:.4f}°".format(beta))
print("r = {:.4f} m".format(r))
print("---------------------------------------------")

# Terceiro passo: Obter os adimensionais

print("Cálculo dos adimensionais")
print("---------------------------------------------")

delta = float(input("Ângulo de fricção solo-metal (delta, em graus): "))
phi = float(input("Ângulo de atrito interno (phi, em graus): "))
rho = float(input("Valor de rho (em graus): "))

ngamma = (r/(2*d) * (1 + (2 * r)/(3 * w) * sin(rad(rho))))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * (tan(rad(beta + phi)))**(-1))
nq = ((r/d) * (1 + (r/w) * sin(rad(rho))))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * (tan(rad(beta + phi)))**(-1))
nca = (1 - (tan(rad(alpha)))**(-1) * (tan(rad(beta + phi)))**(-1))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * (tan(rad(beta + phi)))**(-1))
nc = (1 + tan(rad(beta))**(-1) * tan(rad(beta + phi))**(-1) * (1 + (r/w) * sin(rad(rho))))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * tan(rad(beta + phi))**(-1))
na = (tan(rad(beta)) + (tan(rad(beta + phi)))**(-1))/(cos(rad(alpha + delta)) + sin(rad(alpha + delta)) * (tan(rad(beta + phi)))**(-1))

print("-------------------------------------------------")
print("ngamma = {:.4f}".format(ngamma))
print("nq = {:.4f}".format(nq))
print("nca = {:.4f}".format(nca))
print("nc = {:.4f}".format(nc))
print("-------------------------------------------------")

q = float(input("Valor do carregamento (q, em Pa): "))
c = float(input("Valor de c (em Pa): "))
ca = float(input("Valor de ca (em Pa): "))
gamma = float(input("Peso específico (gamma, em N/m³): "))

print("-------------------------------------------------")
v = float(input("Velocidade de operação (km/h): "))
v /= 3.6
print("-------------------------------------------------")

vc = sqrt(5 * 9.81 * d) # velocidade crítica 

if v <= vc:
  h = (gamma * dc**(2) * ngamma + c * dc * nc + q * dc * nq) * (w + dc * (m - (m - 1)/3)) * sin(rad(alpha + delta))
  vn = -((gamma * dc**(2) * ngamma + c * dc * nc + q * dc * nq) * (w + dc * (m - (m - 1)/3))) * cos(rad(alpha + delta))
  print("v <= vc = {:.2f} km/h, logo v não influencia na força horizontal (H) requerida".format(vc * 3.6))
else:
  h = ((gamma * dc**(2) * ngamma + c * dc * nc + q * dc * nq) * (w + dc * (m - (m - 1)/3)) + (gamma * v**(2) * na * dc * (w + .6 * d)/9.81)) * sin(rad(alpha + delta))
  vn = -((gamma * dc**(2) * ngamma + c * dc * nc + q * dc * nq) * (w + dc * (m - (m - 1)/3)) + (gamma * v**(2) * na * dc * (w + .6 * d)/9.81)) * cos(rad(alpha + delta))
  print("v > vc = {:.2f} km/h, logo v influencia na força horizontal (H) requerida".format(vc * 3.6))

print("H = {:.4f} N".format(h))
print("V = {:.4f} N".format(vn))
print("-------------------------------------------------")

# Encontrar Htotal do implemento

print("---------------------------------------------------------------------")
s = float(input("Espaçamento entre ferramentas (m): "))
n = int(input("Número de ferramentas: "))
print("---------------------------------------------------------------------")
di = dc - s/2 # profundidade da ferramenta virtual

if v <= vc:
  hti = (gamma * di**(2) * ngamma + c * di * nc + q * di * nq) * (w + di * (m - (m - 1)/3)) * sin(rad(alpha + delta))
  vti = -((gamma * di**(2) * ngamma + c * di * nc + q * di * nq) * (w + di * (m - (m - 1)/3))) * cos(rad(alpha + delta))
else:
  hti = ((gamma * di**(2) * ngamma + c * di * nc + q * di * nq) * (w + di * (m - (m - 1)/3)) + (gamma * v**(2) * na * di * (w + .6 * d)/9.81)) * sin(rad(alpha + delta))
  vti = -((gamma * di**(2) * ngamma + c * di * nc + q * di * nq) * (w + di * (m - (m - 1)/3)) + (gamma * v**(2) * na * di * (w + .6 * d)/9.81)) * cos(rad(alpha + delta))

if s < 2 * d:
  htotal = h * n - (n - 1) * hti
  print("Há interação entre as ferramentas.")
else:
  htotal = h * n
  print("Não há interação entre as ferramentas")

print("---------------------------------------------------------------------")
print("Profundidade da ferramenta virtual (di) = {:.4f} mm".format(di * 1000))
print("Força horizontal da ferramenta virtual (Hti) = {:.4f} N".format(hti))
print("Força vertical da ferramenta virtual (Vti) = {:.4f} N".format(vti))
print("Htotal = {:.4f} N".format(htotal))
print("---------------------------------------------------------------------")