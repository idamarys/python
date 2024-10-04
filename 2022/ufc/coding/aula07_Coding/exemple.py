'''NumeroDeAlunos = int(input("Digite o número de alunos da turma: "))
SomaDasNotas = 0
for x in range(NumeroDeAlunos):
    SomaDasNotas += (input("Digite a nota do aluno: "))

media = SomaDasNotas/NumeroDeAlunos
print(media)''' 

#WHILE_PROBLEM

'''n = int(input("Insira um valor: "))
variavel = 1
while (variavel <= n):
    print(variavel)
    variavel+=1

while (variavel > 0): INFINITO
variavel = o: primeiro valor a ser printado
(VARIAVEL <= N) 
variavel +=2: vai de dois em dois. EX.: 0, 2, 4...
variavel +=2 == variavel = variavel + 2'''

'''n = 2222
x1 = n%10
x2 = (n%100 - n%10) /10
x3 = (n%1000 - n%100) /100
x4 = (n%10000 - n%1000) /1000
x5 = (n%100000 - n%10000) /10000

n = 222224522
 i = 0
 temp = n

while temp > 0:
    i += 1
    temp -= temp%(10**i)
    print(i)

cont = 0
j = 1
while j <= i:
    x = ((n%(10**j))) - (n%(10**(j-1))))/(10**(J-1)) #isso é a mesma coisa que o de cima
    if x ==2: 
        cont += 1
print("O numero 2 aparece %d vezes" %cont)'''