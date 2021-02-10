sal = float(input("Digite seu salario atual: "))
anos = int(input("Digite o numero de anos trabalhados: "))

if(anos > 10 and sal > 2000):
    sal = sal + 500
elif(sal <= 500 and anos < 1):
    sal = sal + ((sal / 100) * 25)
elif(sal <= 1000 and anos <= 3):
    sal = sal + ((sal / 100) * 20) + 100
elif (sal <= 1500 and anos <= 6):
    sal = sal + ((sal / 100) * 15) + 200
elif (sal <= 2000 and anos <= 10):
    sal = sal + ((sal / 100) * 10) + 300

print("Seu novo salario é {} ".format(sal))