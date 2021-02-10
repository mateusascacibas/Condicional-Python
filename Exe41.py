alt = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (alt * alt)

if(imc <= 18.5):
    print("Abaixo do Peso")
elif(imc <= 24.9):
    print("Saudável")
elif(imc <= 29.9):
    print("Peso em Excesso")
elif(imc <= 34.9):
    print("Obesidade grau 1")
elif(imc <= 39.9):
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")