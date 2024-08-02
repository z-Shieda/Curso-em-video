import math

x = (float(input("Digite o Angulo")))

cos = math.cos(math.radians(x))
seno = math.sin(math.radians(x))
tang = math.tan(math.radians(x))

print("O valor do Cosseno é {} \n Do Seno é {} \n E da Tangente é {}".format(cos, seno, tang))
