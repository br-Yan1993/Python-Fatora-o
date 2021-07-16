valor = int(input("Qual o valor a ser fatorado?: "))

divisor = valor
vet_res = []
vet_div = []
vet_res.append(valor)
while (valor != 1):
    if (valor %2 == 0):
        vet_res.append(valor//2)
        valor = vet_res[-1]
        vet_div.append(2)
    elif (valor % 3 == 0):
        vet_res.append(valor//3)
        valor = vet_res[-1]
        vet_div.append(3)
    elif (valor % 5 == 0):
        vet_res.append(valor//5)
        valor = vet_res[-1]
        vet_div.append(5)
    elif (valor % 7 == 0):
        vet_res.append(valor//7)
        valor = vet_res[-1]
        vet_div.append(7)
    elif (valor % 11 == 0):
        vet_res.append(valor//11)
        valor = vet_res[-1]
        vet_div.append(11)
    elif (valor % 13 == 0):
        vet_res.append(valor//13)
        valor = vet_res[-1]
        vet_div.append(13)
    elif (valor % 17 == 0):
        vet_res.append(valor//17)
        valor = vet_res[-1]
        vet_div.append(17)
    elif (valor % 19 == 0):
        vet_res.append(valor//19)
        valor = vet_res[-1]
        vet_div.append(19)
    elif (valor % 23 == 0):
        vet_res.append(valor//23)
        valor = vet_res[-1]
        vet_div.append(23)
    elif (valor % 29 == 0):
        vet_res.append(valor//29)
        valor = vet_res[-1]
        vet_div.append(29)
    else:
        valor = vet_res[-1]
        vet_res.append(valor//valor)
        vet_div.append(valor)

#print(vet_res)
#print(vet_div)
print('Valores Fatorados:')

for i in vet_res:
    q = i*1
    print(q)

print('\nDivisores Primos de {}:'.format(divisor))
for j in vet_div:
    p = j*1
    print(p)