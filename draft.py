ferr = input("[N]arrow point, 30 cm [W]inged point: ") 
texture = input("[F]ino, [M]édio ou [G]rosseiro: ")
s = float(input("Velocidade (km/h): "))
w = float(input("Número de ferramentas (w, inteiro) ou largura da máquina (w, em metros): "))
t = float(input("Profundidade (t, em cm): ")) # profundidade

# f depende do tipo de solo

# Parâmetros da máquina no SI
if ferr == "N":
  a = 226
  b = 0
  c = 1.8
else:
  a = 294
  b = 0
  c = 2.4


if texture == "F":
  f = 1
elif texture == "M":
  f = .7
else:
  f = .45

draft = f * (a + b * s + c * s**(2)) * w * t

print("Força de arrasto requerida: {:.2f} N".format(draft))

# Estimativa de potência
p = draft * s / 3.6
print ("Potência requerida = {:.2f} W = {:.2f} cv".format(p, p /746))