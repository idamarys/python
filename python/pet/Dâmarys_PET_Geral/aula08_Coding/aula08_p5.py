a = int(input("Insira o primeiro elemento: "))
r = int(input("Insira a razão da PA: "))
N = int(input("Insira a quantidade desejada: "))

print(a)

for i in range(N - 1):
    a += r
    PA = a + r
    print(a)

print(PA)