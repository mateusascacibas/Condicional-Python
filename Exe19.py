num = int(input(("Digite um numero: ")))

if((num % 3 == 0) and (num % 5 == 0)):
    print("Divisivel por 5 e 3")
elif((num % 3 == 0)):
    print("Divisivel somente por 3")
elif((num % 5 == 0)):
    print("Divisivel somente por 5")
else:
    print("Não é divisivel por 3 e nem 5")