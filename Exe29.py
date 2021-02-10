import numpy as np

num_perg = 0
resp = 0
acerto = 0
erro = 0

while(num_perg < 5):
    n1 = np.random.randint(1, 100)
    n2 = np.random.randint(1, 100)
    total = n1 + n2
    print("Qual o valor de " + str(n1) + " + " + str(n2) + " ? ")
    resp = int(input())

    if(resp == total):
        acerto += 1
        print("Resposta certa! \n")
    else:
        erro += 1
        print("Errado, resposta certa é " + str(total))

    num_perg += 1

print("Você acertou: " + str(acerto) )
print("Você errou: " + str(erro))

