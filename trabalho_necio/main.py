from Grafo import Grafo

#Ler dados
vetor_entrada = []
with open('coloracao-inst13', 'r') as arquivo:
    for linha in arquivo:
        x = linha.strip()
        v = x.split()
        vetor_entrada.append(v)


#Insira a quantidade de Vértices
vertice = int(vetor_entrada[0][0])

#Criando Grafo
grafo = Grafo(vertice)

#Inserindo arestas
arestas = (len(vetor_entrada) - 1)


for i in range(1, (arestas + 1), 1):
    a = int(vetor_entrada[i][0])
    b = int(vetor_entrada[i][1])
    peso = 1

    grafo.adicionaAresta(a, b, peso)

#mostra a matriz
grafo.mostraMatriz()

#mostra pares de vertices e cores
saida = grafo.coloracao()

print("-> [ Vértice , Cor ] é :"+ str(saida))

#quantidade de cores
maior = 0
for i in saida:
    if(i[1] > maior):
        maior = i[1]

print("\nO número de cores usadas foram: "+ str(maior))
