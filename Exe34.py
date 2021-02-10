nota = float(input("Digite a nota: "))
faltas = int(input("Digite as faltas: "))

if(nota <= 3.9):
    print("E")
elif(nota <= 4.9):
    if(faltas <= 20):
        print("D")
    else:
        print("E")
elif(nota <= 7.4):
    if(faltas <= 20):
        print("C")
    else:
        print("D")
elif(nota <= 8.9):
    if(faltas < 20):
        print("B")
    else:
        print("C")
else:
    if(faltas < 20):
        print("A")
    else:
        print("B")