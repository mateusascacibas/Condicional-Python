media = 0

print("Digite duas notas: ")
n1 = int(input())
n2 = int(input())

if (n1 <= 10.0) and (n2 <= 10.0):
    if (n1 >= 0) and (n2 >= 0):
        media = (n1 + n2) / 2
        print("Média é: ")
        print(media)
else:
    print("Digite notas validas")