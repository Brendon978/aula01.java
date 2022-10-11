maior = 0
menor = 0
media = 0

def pilha():
    num = list(map(int, input("Digite os números separados por espaço: ").split()))
    print(f"Maior: {max(num)}")
    print(f"Menor: {min(num)}")
    print(f"Média: {sum(num) / len(num)}")

pilha()
