total = 0.0
op =  int(input("Digite um numero para opção \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair \n"))

while((op < 6) and (op > 0)):

    if(op == 5):
        print("Obrigado!")
        break
    else:
        print("Entre dois numeros: ")
        n1 = int(input("Numero 1: "))
        n2 = int(input("Numero 2: "))
        if(op == 1):
            total = n1 + n2
        elif(op == 2):
            total = n1 - n2
        elif(op == 3):
            total = n1 * n2
        else:
            if(n1 == 0 or n2 == 0):
                print("Divisão por zero não existe.")
                total = "0"
            else:
                total = n1 / n2

    print("O resultado é ")
    print(total)
    op = int(input(
        "Digite um numero para opção \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair \n"))

