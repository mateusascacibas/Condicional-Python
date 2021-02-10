basemaior = float(input("Digite a base maior: "))
basemenor = float(input("Digite a base menor: "))
altura = float(input("Digite a altura: "))

if(basemaior > 0 and basemenor > 0):
    area = ((basemaior + basemenor) * altura) / 2
else:
    print("Invalido.")

print("A area do trapezio é: {} ".format(area))