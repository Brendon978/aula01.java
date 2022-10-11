txt = str(input("Digete uma palavra: "))
invertido = txt[::-1]

if invertido == txt:
    print("A palavra digitada é um palindromo")

else:
    print("A palavra digitada não é um palindromo")
