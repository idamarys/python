def mult_list(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] * mult_list(lista[1:])

print(mult_list([1, 3, 5, 7, 9]))