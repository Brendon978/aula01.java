dist = [[0,1611,5298,4397,3250,2100,2933],[1611,0,5763,4865,2805,1389,3127],[5298,5763,0,901,4374,5009,3971],[4397,4865,901,0,3473,4023,3070],[3250,2805,4374,3473,0,1649,429],[2100,1389,5009,4023,1649,0,1962],[2933,3127,3971,3070,429,1962,0]]
linhas = ['BELÉM','FORTALEZA','MANAUS','PORTO VELHO','RIO DE JANEIRO','SALVADOR','SÃO PAULO']
colunas = linhas
dt = 0
cid1 = input('Digite a cidade de origem: ')
lin = linhas.index(cid1)
while True:
    cid1 = input('Digite a próxima cidade: ')
    if cid1 != 'XX':
        col = colunas.index(cid1)
        dt += dist[lin][col]
        lin = col
    else:
        break
print('A distância total a ser percorrida são {} KM'.format(dt))