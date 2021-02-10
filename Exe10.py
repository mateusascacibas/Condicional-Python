print("Digite a altura ")
alt = float(input())
print("Digite seu sexo 'M' ou 'F'")
sexo = input()

if sexo == "M":
    ideal = (72.7 * alt) - 58
    print("Peso ideal é: ")
    print(ideal)
else:
    ideal = (62.1 * alt) - 44.7
    print("Peso ideal é: ")
    print(ideal)