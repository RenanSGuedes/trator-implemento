import math

d = float(input("Profundide da ferramenta (m): "))
w = float(input("Largura da ferramenta (m): "))

delta = float(input("Valor de delta (em graus): ")) * 180/math.pi
phi = float(input("Valor de phi (em graus): ")) * 180/math.pi

# Primeiro passo: Tipo de ferramenta

if d/w < 1:
  print("Blade")
elif (d/w >= 1 and d/w < 6):
  print("Narrow tine")
else:
  print("Very narrow tine")

# Segundo passo: Acha o valor de beta crítico
alpha = float(input("Ângulo de ataque (alpha, em graus): "))# em radianos
m = 4.0704 - (0.0940983 * alpha) + (0.00149667 * alpha**2) - (0.0000121924 * alpha**3) + (3.963 * 10**(-8) * alpha**4)

beta = math.atan(1/(m - (math.tan(alpha * math.pi / 180))**(-1))) * 180/math.pi

# Terceiro passo: Obter os adimensionais

r = d * ((math.tan(alpha))**(-1) + (math.tan(beta))**(-1))

ngamma = (r/(2*d) * (1 + (2 * r)/(3 * b) * math.sin(rho)))/(math.cos(alpha + delta) + math.sin(alpha + delta) * (math.tan(beta + phi))**(-1))

print(m, beta, r)