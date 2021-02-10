op = int(input("Digite 1 para iniciar o pedido, 0 para cancelar. "))
item = 0
pedido = [0, 100]
valor = 0.0
i = 0
while(op != 0):
    cod = int(input("Qual o codigo do produto que quer? "))

    if(cod == 100):
        pedido.append("Cachorro Quente - 1,20")
        valor += 1.20
    elif(cod == 101):
        pedido.append("Bauru Simples - 1,30")
        valor += 1.30
    elif(cod == 102):
        pedido.append("Bauru Com Ovo - 1,50")
        valor += 1.50
    elif(cod == 103):
        pedido.append("Hamburguer - 1,20")
        valor += 1.20
    elif (cod == 104):
        pedido.append("Cheeseburguer - 1,70")
        valor += 1.70
    elif (cod == 105):
        pedido.append("Suco - 2,20")
        valor += 2.20
    elif (cod == 106):
        pedido.append("Refrigerante - 1,00")
        valor += 1.00
    else:
        print("Código errado. ")


    op = int(input("Deseja pedir mais alguma coisa? 1 para sim e 0 para não. "))

print("Seu pedido ficou assim: ")

for i in range(len(pedido)):
    print(pedido[i])


print(" saindo no total de " + str(valor))
