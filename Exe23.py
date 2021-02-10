bi = int(input("Digite um ano: "))

if(bi % 400 == 0 or (bi % 4 == 0 and bi % 100 != 100)):
    print("Ano Bissexto")
else:
    print("Ano não bissexto")