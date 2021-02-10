maior = 0
diferenca = 0

print("Digite um numero")
n1 = int(input())
print("Digite outro numero")
n2 = int(input())

if n1 > n2:
    maior = n1
    diferenca = n1 - n2
elif n2 > n1:
    maior = n2
    diferenca = n2 - n1

if n1 == n2:
    print("Numero iguais, sem diferença")
else:
    print("Numero maior: ")
    print(maior)
    print("Diferença: ")
    print(diferenca)

