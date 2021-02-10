day = int(input("Digite um numero: "))

if(day > 12 or day < 0):
    print("Numero invalido. Digitar numero entre 1 e 12")
else:
    if(day == 1):
        print("Janeiro.")
    elif(day == 2):
        print("Fevereiro.")
    elif(day == 3):
        print("Março.")
    elif(day == 4):
        print("Abril.")
    elif(day == 5):
        print("Maio.")
    elif(day == 6):
        print("Junho.")
    elif (day == 7):
        print("Julho.")
    elif (day == 8):
        print("Agosto.")
    elif (day == 9):
        print("Setembro.")
    elif (day == 10):
        print("Outubro.")
    elif (day == 11):
        print("Novembro.")
    else:
        print("Dezembro")


