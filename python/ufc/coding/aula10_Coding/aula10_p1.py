lista = []

def multiplicador(lista):
    mult = 1
    for item in lista:
        mult = item * mult
    return mult

while -1 not in lista:
    lista.append(int(input("Insira um número a ser multiplicado (Insira '-1' para parar): ")))
lista.remove(-1)

print(multiplicador(lista))