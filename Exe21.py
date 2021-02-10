op = int(input(" 1 - Soma de 2 números \n "
               "2 - Diferença entre 2 numeros (maior pelo menor) \n "
               "3 - Produto entre 2 números \n "
               "4 - Divisão entre 2 números \n"))
resultado = 0

if(op < 1 or op > 4):
    print("Erro, opção invalida.")
else:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))

    if(op == 1):
        resultado = n1 + n2
        print("O resultado da soma é {} ".format(resultado))
    elif(op == 2):
        if(n1 > n2):
            resultado = n1 - n2
        else:
            resultado = n2 - n1


        print("A diferença entre os dois é de {} ".format(resultado))
    elif(op == 3):
        resultado = n1 * n2

        print("O produto dos dois é de {} ".format(resultado))
    elif(op == 4):
        if(n1 == 0 or n2 == 0):
            print("Erro, divisão por 0 não existe.")
        else:
            resultado = n1 / n2
            print("O resultado da divisão é {} ".format(resultado))
