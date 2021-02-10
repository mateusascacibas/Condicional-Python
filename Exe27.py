idade = int(input("Digite a idade: "))

if(idade >= 5 and idade <= 7):
    print("Infantil A")
elif(idade <= 10):
    print("Infantil B")
elif(idade <= 13):
    print("Infantil C")
elif(idade <= 17):
    print("Infantil D")
else:
    print("Senior")
