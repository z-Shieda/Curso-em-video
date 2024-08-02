real = float(input("Digite quantos reais você tem"))
if real >= (5.62):
    convert = real * 0.18
    print("Você pode comprar {} unidade(s) de dolar".format(convert))
else:
    print("Você não possui saldo para efetuar a compra")

