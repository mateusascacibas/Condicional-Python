n1 =  int(input("Digite a nota 1 (Trabalho de Lab): "))
n2 =  int(input("Digite a nota 2 (Avaliacao Semestral): "))
n3 =  int(input("Digite a nota 3 (Exame FInal): "))

media = (( n1 * 2 )+ (n2 * 3) + (n3 * 5)) / 10

if(media <= 2.9):
    print("Reprovado. ")
elif (media <= 4.9):
    print("Recuperação. ")
else:
    print("Aprovado. ")