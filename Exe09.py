print("Digite seu salario: ")
sal = float(input())
print("Digite a prestação do emprestimo: ")
emp = float(input())

por = (sal / 100) * 20

if emp > por:
    print("Emprestimo não concedido")
else:
    print("Emprestimo concedido")

