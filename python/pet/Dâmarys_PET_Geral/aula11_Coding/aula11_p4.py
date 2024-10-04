'''num_Positv = int(input("Insira um número positivo: "))

def num_Pos(Positivo):
    if num_Pos > 0 and :
        return True
    else:
        return False

print()'''

def primo (numPrimo, divisor = 2):
    if divisor == numPrimo:
        return True
    elif numPrimo % divisor > 0:
        return primo(numPrimo, divisor + 1)
    else:
        return False

print(primo(541))