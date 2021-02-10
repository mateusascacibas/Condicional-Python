import math

n = int(input("Digite um numero positivo para calcular raiz, negativos serao elevados ao quadrado "))

if(n <= 0):
    print(n * n)
else:
    print(math.sqrt(n))