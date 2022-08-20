numeros = int()
par = []
impar = []
lista = []
tl = []

for v in range(20):
    numeros = int(input("Digite os números: "))
    resto = numeros % 2
    if resto== 0:
        par.append(numeros)
    else:
        impar.append(numeros)

    lista.append(numeros)
    tl.append(numeros)
tl = sorted(tl)

print("Estes são todos os números: {}\n".format(lista))
print("Todos os números em ordem crescente: {}\n".format(tl))
print("Todos os números em ordem decrescente: {}\n".format(sorted(tl, reverse = True)))
print("Pares: {}\n".format(par))
print("Pares em ordem crescente: {}\n".format(sorted(par)))
print("Impares: {}\n".format(impar))
print("Impares em ordem crescente: {}\n".format(sorted(impar)))
