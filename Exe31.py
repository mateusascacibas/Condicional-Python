alt = int(input("Digite sua altura em (CM): \n "))
peso = float(input("Digite seu peso: \n "))

if(alt < 120):
    if(peso <= 60):
        print("Sua classificação é A. ")
    elif(peso <= 90):
        print("Sua classificação é D. ")
    else:
        print("Sua classificação é G")
elif(alt <= 170):
    if (peso <= 60):
        print("Sua classificação é B. ")
    elif (peso <= 90):
        print("Sua classificação é E. ")
    else:
        print("Sua classificação é H")
else:
    if (peso <= 60):
        print("Sua classificação é C. ")
    elif (peso <= 90):
        print("Sua classificação é F. ")
    else:
        print("Sua classificação é I")

