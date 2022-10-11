expr = str(input("digite a expressão desejada: "))
parenteses = []

for simb in expr:
    if simb == "(":
        parenteses.append("(")
    elif simb == ")":
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(")")
            break

if len(parenteses) == 0:
    print("A expressão digitada está válida!")

else:
    print("A expressão digitada não é válida!")
