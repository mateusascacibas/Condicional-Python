val = float(input("Digite o valor da venda: "))
perc = ((val/100) * 14)
if(val < 20000):
    com = 400 + perc
elif(val < 40000):
    com = 500 + perc
elif(val < 60000):
    com = 550 + perc
elif(val < 80000):
    com = 600 + perc
elif(val < 100000):
    com = 650 + perc
else:
    com = 700 + ((val / 100) * 15)

print(com)