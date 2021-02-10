maior = 0
print("Digite um numero: ")
um = int(input())
print("Digite outro numero: ")
dois = int(input())

if um > dois:
    maior = um
elif dois > um:
    maior = dois

if um == dois:
    print("Ambos são iguais")

else:
    print("O maior é ")
    print(maior)


