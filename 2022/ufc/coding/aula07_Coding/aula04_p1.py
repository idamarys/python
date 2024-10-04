import time
'''NO MEU range, EU TENHO QUE COLOCAR O NÚMERO QUE EU QUERO QUE INICIE, 
O NÚMERO QUE EU LEREI E, SE EU QUISER PRINTAR ATÉ ESSE NÚMERO, SOMAR ELE A 1.
SE ISSO TUDO ESTÁ INCLUSO EM x, PRINTAREMOS O x, logo estaremos printando tudo o que queremos'''
n = int(input("Digite um número inteiro e positivo: "))
for x in range(1, n + 1):
    print(x)
    time.sleep(0.5)