import time
n = int(input("Digite a quantidade múltiplos que você deseja: "))
x = int(input("Digite um número: "))

for z in range(1, n+1):
    z *= x
    print(z)
    time.sleep(0.5)
