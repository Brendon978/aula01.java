km = [[0,1611,5298,4397,3250,2100,2933],[1611,0,5763,4865,2805,1389,3127],[5298,5763,0,901,4374,5009,3971],[4397,4865,901,0,3473,4023,3070],[3250,2805,4374,3473,0,1649,429],[2100,1389,5009,4023,1649,0,1962],[2933,3127,3971,3070,429,1962,0]]
cidades = ['BELÉM','FORTALEZA','MANAUS','PORTO VELHO','RIO DE JANEIRO','SALVADOR','SÃO PAULO']
colunas = cidades

list = []

def cidade_origem(list):
    origem = str(input("Digite o nome da cidade"))
    linha = cidades.index(origem)

def cidade_destino(list):
    destino = str(input("Digite o nome da cidade"))
    coluna = km.index(destino)

while True:

    print("1- cidade de origem")
    print("2- cidade de destino")

    menu = int(input("escolha uma opção"))

    match menu:
        case 1:
            cidade_origem(list)            
        case 2:
            cidade_destino(list)
    if km[linha][coluna] != 0:
        print('A distância entre as duas cidades é de {} KM'.format(km[linha][coluna]))
    else:            
        break