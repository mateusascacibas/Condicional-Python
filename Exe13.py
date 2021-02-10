n1 =  int(input("Digite a nota 1: "))
n2 =  int(input("Digite a nota 2: "))
n3 =  int(input("Digite a nota 3: "))

media = (n1 + n2  + (n3 * 2)) / 3

if(media >= 60):
    print("Aprovado. ")
else:
    print("Reprovado")
