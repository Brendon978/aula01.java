numeros = int()
lista = []

def add_inicio(lista):      
    numeros = int(input("Digite um numero para adicionar ao inicio: "))
    if lista == False:
        aux = lista - 1
        lista += [0]
        while aux >= 0:
            lista[aux + 1] = lista[aux]
            aux = aux - 1
        lista[0] = numeros
    else:
        lista += [numeros]       

def add_fim(lista):
    numeros = int(input("Digite um numero para adicionar ao fim: "))
    lista += [numeros]

def re_inicio(lista):
    lista.pop(0)

def re_fim(lista):
    lista.pop(len(lista) - 1)

def verificar_lista(lista):
    if len(lista) > 0:
        print("Lista não está vazia")                
    else:
        print("A lista está vazia")

while True: 
    print("1 Adiciona ao inicio")
    print("2 Adiciona ao fim")
    print("3 Remover do inicio")
    print("4 Remover do fim")
    print("5 Verificar lista")
    print("6 Finalizar o programa\n")

    menu = int(input("Escolha uma opção: "))
    if menu >= 7:
        print("Opção invalida!")
        print("escolha uma opção valida!\n")

    match menu:  
        case 1:
            add_inicio(lista)
            
        case 2:
            add_fim(lista)
            
        case 3:
            re_inicio(lista)
                        
        case 4:
            re_fim(lista)
            
        case 5:
            verificar_lista(lista)
            print("Estes numeros já estão dentro da lista: {}\n".format(lista))

        case 6:
            menu = int(input("Fim do programa!"))
            break;
        