list = int(input("Digite o tamanho da pilha: "))
pilha = []

for p in range(list):
    num = int(input("Digite os numeros: "))
    pilha.append(num)
print(pilha)
print(sorted(pilha))
