day = int(input("Digite um numero: "))

if(day > 7 or day < 0):
    print("Numero invalido. Digitar numero entre 1 e 7")
else:
    if(day == 1):
        print("Domingo.")
    elif(day == 2):
        print("Segunda Feira.")
    elif(day == 3):
        print("Terça Feira.")
    elif(day == 4):
        print("Quarta Feira.")
    elif(day == 5):
        print("Quinta Feira.")
    elif(day == 6):
        print("Sexta Feira.")
    else:
        print("Sábado")


