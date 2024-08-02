q_km = float(input("Quantos KM foram percorridos ?"))
dia = int(input("Quantos dias o carro foi alugado ?"))
calc_km = q_km * 0.15
calc_dia = dia * 60

total = calc_km + calc_dia

print("O total a ser pago é R${}".format(total))