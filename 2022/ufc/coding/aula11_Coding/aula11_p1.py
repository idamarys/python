'''expoente = int(input("Digite o expoente: "))
base = int(input("Digite a base: "))

def exp(base, expoente):
    if expoente == :
        return potencia[0]
    else:
        return potencia[0] + mult_list(potencia[1:])'''


def potencia (m, n):
    if n < 1:          #casa base
        return 1
    else:
        return m * potencia(m, n -1)

print(potencia(2, 10))