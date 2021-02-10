preco_fabrica = float(input("Digite o preço de fabrica: "))

if(preco_fabrica <= 12000):
    preco_total = preco_fabrica + ((preco_fabrica / 100) * 5)
elif(preco_fabrica <= 25000):
    preco_total =  preco_fabrica + ((preco_fabrica / 100) * 10) + ((preco_fabrica / 100) * 15)
else:
    preco_total =  preco_fabrica + ((preco_fabrica / 100) * 15) + ((preco_fabrica / 100) * 20)

print("Preço total {}".format(preco_total))