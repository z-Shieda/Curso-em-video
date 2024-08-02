
preco = float(input("Digite o preco do produto"))
cupom = input("Caso possua algum cupom, digite abaixo")
desconto_aplicado = preco * 0.95
if cupom == "desconto5":
    print("O preco do produto com desconto é R$:{} ".format(desconto_aplicado))
else:
    print("O preco do produto é R$:{} ".format(preco))
