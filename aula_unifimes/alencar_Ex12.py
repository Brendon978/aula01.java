P1 = list(map(int, input("Digite os números separados por espaço: ").split()))
P2 = list(map(int, input("Digite os números separados por espaço: ").split()))

if len(P1) > len(P2):
    print ("P1 é maior que P2!")

if len(P1) < len(P2):
    print ("P2 é maior que P1!")

elif len(P1) == len(P2):
    print("P1 e P2 são do mesmo tamanho!")
