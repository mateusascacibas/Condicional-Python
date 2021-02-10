preco = float(input("Digite o preço: "))

if(preco < 50):
    var = 5
elif(preco <= 100):
    var = 10
else:
    var = 15

preco += (var / preco) * 100

if(preco < 80):
    print("Barato.")
elif(preco <= 120):
    print("Normal")
elif(preco <= 200):
    print("Caro")
else:
    print("Muito caro")