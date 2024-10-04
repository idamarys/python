'''palavras_a_serem_cortadas = ['Rafael', 'Yasser', 'Tom']

def cortadorDePalavras (string):
    stringCortada = []
    for letra in string:
        stringCortada.append(letra)
    return stringCortada

cortadorDePalavras(palavras_a_serem_cortadas[0])    
cortadorDePalavras(palavras_a_serem_cortadas[1])
cortadorDePalavras(palavras_a_serem_cortadas[2])
for palavra in palavras_a_serem_cortadas:
    print(cortadorDePalavras(palavra))


for palavra in range (0,3):
    print(cortadorDePalavras(palavra))'''

#exemplo2

'''palavras_a_serem_cortadas = ['Rafael', 'Yasser', 'Tom']

def cortadorDePalavras (strings):
    for string in strings:
        stringCortada = []
    for letra in string:
        stringCortada.append(letra)
    print(stringCortada)

cortadorDePalavras(palavras_a_serem_cortadas)'''

'''cortadorDePalavras(palavras_a_serem_cortadas[0])    
cortadorDePalavras(palavras_a_serem_cortadas[1])
cortadorDePalavras(palavras_a_serem_cortadas[2])

for palavra in palavras_a_serem_cortadas:
    print(cortadorDePalavras(palavra))

    
for palavra in range (0,3):
    print(cortadorDePalavras(palavra))'''

#exemplo3

'''listaDePessoas = ['Rafael', 'Yasser', 'Gabriel', 'Elias']

def apagarPessoaDaLista (nomeDaPessoa, listaDePessoas):
    if nomeDaPessoa in listaDePessoas:
        listaDePessoas.remove(nomeDaPessoa)
    else:
        print('Pessoa não encontrada.')

apagarPessoaDaLista('Rafael', listaDePessoas)
print(listaDePessoas)
apagarPessoaDaLista('Thiago', listaDePessoas)'''

#exemplo4

'''def printarIngredientes(*ingredietes):
    print(f'A pizza será feita com os seguintes ingredientes: {ingredientes} ')
    for ingrediente in ingredientes:
        print(ingrediente)

printarIngredientes('Toamte', 'Mulher', 'peperone', 'queijo', 'baicon')'''

'''def ingredientesDaPizza(numeroDoPedido, **ingredientes):
    print(f'Ingredientes do pedido {numeroDoPedido}')
    for key, value in ingredientes.items():
        print(f'{key}: {value})

ingredientesDaPizza(12, sabor = 'Queijo', borda = 'Recheada', com_cebola = True)'''

#exemplo5

'''def porcentagem (preco):
    return preco*0.3

porcentagem2 = lambda preco: porcentagem(preco)

print(porcentagem2(10))'''

#exemplo6

'''def contador (n):
    temp = n
    i = 0
    cont = 0

    while temp > 0:
        i += 1
        temp -= temp%(10**i)'''