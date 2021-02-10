dia = int(input("Digite dia "))
mes =  int(input("Digite mês "))
ano = int(input("Digite ano "))

if(mes <= 12 and mes > 0):
    if(dia <= 31 and dia > 0):
        if(mes == 2):
            if((ano%4==0 and ano%100!=0) or (ano%400==0)):
                if(dia > 29):
                    print("Erro, fevereiro em anos bissextos tem 29 dias")
            else:
                if(dia > 28):
                    print("Erro, fevereiro tem 28 dias")
    else:
        print("Data invalida.")
else:
    print("Data invalida.")