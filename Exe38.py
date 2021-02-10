dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

dia_ap = 0
mes_ap = 0
ano_ap = 0
if(ano < 2021):
    if(ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
        if(mes == 2):
            if(dia > 0 and dia <30 ):
                print("Data valida.")
    elif(mes > 0 and mes < 13):
        if(dia > 0 and dia < 32):
            print("Data valida.")
