lista = []

def fatorar(a, show):
    mult = num
    for i in range(num, 1, -1):
        mult = mult * i
        if show == False:
            print(mult)
    return mult

num = int(input("Insira um número a ser fatorado: "))
show = int(input("Insira '1' para mostrar o cálculo ou '0' para não mostrar o cálculo: "))
if show == 1:
    a = True
else:
    a = False

print(fatorar(a, show))