import math

n = int(input("Digite um numero, negativos serão invalidados. "))

if(n < 0):
    print("Numero invalido.")
else:
    print(math.sqrt(n))