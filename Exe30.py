n1 = int(input("Digite 1 numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite o ultimo numero: "))

maior = 0
menor = 0
meio = 0
if(n1 > n2 and n1 > n3):
    maior = n1
    if(n2 > n3):
        meio = n2
        menor = n3
    else:
        meio = n3
        menor = n2
elif(n2 > n3 and n2 > n1):
    maior = n2
    if(n3 > n1):
        meio = n3
        menor = n1
    else:
        meio = n1
        menor = n3
else:
    maior = n3
    if(n1 > n2):
        meio = n1
        menor = n2
    else:
        meio = n2
        menor = n1

print("O maior é " + str(maior))
print("O do meio é " + str(meio))
print("O menor é " + str(menor))
