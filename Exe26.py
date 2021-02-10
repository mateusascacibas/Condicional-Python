km = float(input("Digite o percurso em KM: "))
lit = float(input("Quantidade de gasolina: "))

kmpl = km / lit
if(kmpl < 8):
    print("Venda o carro")
elif(kmpl < 11 ):
    print("Economico")

else:
    print("Super economico")