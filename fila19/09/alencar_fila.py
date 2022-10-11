fila = []
def excluir_nota(fila):
    if fila.pop(0):
        print("Nota excluida!")
    elif fila == 0:
        print("A lista de notas está vazia!")
      
   