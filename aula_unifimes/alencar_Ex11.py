pilha = []
n_l = int(input("Insira o número de elementos: \n"))

for l in range(n_l):
        numeros = int(input("Digite os números a serem adicionados a pilha: "))

        pilha.append(numeros)       

print("\nDados inseridos na pilha: {}".format(pilha))
print("pilha em ordem decrescente: {}".format(sorted(pilha, reverse = True)))