def search(lista, item):
    i = 0
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        i = i + 1
        print(i)
        meio = (baixo+alto) //2
        chute = lista[meio]
        if chute == item: 
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
lista = [1, 3, 5, 7, 10, 9, 25]


# print(search(lista, 25))
