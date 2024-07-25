def pesquisa_binario(lista, item, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    if inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio
        if item < lista[meio]:
            return pesquisa_binario(lista, item, inicio, meio - 1)
        else:
            return pesquisa_binario(lista, item, meio + 1, fim)
    return None
    
lista = [2, 2, 4, 7, 11, 21, 23, 30, 41]
print(pesquisa_binario(lista, 22))   
 
''' baixo = 0
    alto= len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) /2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
        
    return None

minha_lista = [1, 3, 5, 7, 9]
print (pesquisa_binario(minha_lista, 3))
print (pesquisa_binario(minha_lista, -1))'''