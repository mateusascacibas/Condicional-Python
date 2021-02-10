val = float(input("Digite o valor: "))
uf = input("Digite a UF do estado: ")

if(uf == "MG"):
    val += (val / 100) * 7
elif(uf == "SP"):
    val += (val / 100) * 12
elif(uf == "RJ"):
    val += (val / 100) * 15
elif(uf == "MS"):
    val += (val / 100) * 8
else:
    print("UF invalida")
print("Valor fica de: ")
print(val)