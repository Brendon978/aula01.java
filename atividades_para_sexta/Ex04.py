numeros = int()
lista = []
n_l = int(input("Insira o número de nós: \n"))

for l in range(n_l):
        numeros = int(input("Digite os números a serem adicionados a lista: "))
        lista.append(numeros)


numeros = int(input("Digite o número a ser adicionado ao inicio da lista: "))
lista.insert(0,numeros)

        
print("\nDados inseridos na lista: {}".format(lista))
