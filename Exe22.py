idade = int(input("Digite sua idade: "))
ts = int(input("Tempo de serviço em anos: "))

if((idade >= 65) or (ts >= 30) or ((idade >= 60) and (ts >= 25))):
    print("Pode aposentar.")
else:
    print("Não pode aposentar.")