from Grafo import Grafo

#Arquivo de entrada
entrada = 'coloracao-teste'

#Ler dados
vetor_entrada = []
with open(entrada, 'r') as arquivo:
    for linha in arquivo:
        x = linha.strip()
        v = x.split()
        vetor_entrada.append(v)


#Lendo quantidade de Vértices
vertice = int(vetor_entrada[0][0])

#Criando Grafo
grafo = Grafo(vertice)

#Lendo quantidade de arestas
arestas = (len(vetor_entrada) - 1)


for i in range(1, (arestas + 1), 1):
    a = int(vetor_entrada[i][0])
    b = int(vetor_entrada[i][1])
    peso = int(vetor_entrada[i][2])

    grafo.adicionaAresta(a, b, peso)

#=========== Saída de dados ================
print("\n\n================= SAÍDA DE DADOS ==================\n\n")
print("-> Quantidade de Vértices: "+ str(vertice))
print("-> Quantidade de Arestas: "+ str(arestas))
print("\n")
print("-> Matriz de Adjascencia: \n\n")
grafo.mostraMatriz()
print("\n\n")

#mostra pares de vertices e cores
saida = grafo.coloracao()

print("-> [ Vértice , Cor ] é :"+ str(saida))

#quantidade de cores
maior = 0
for i in saida:
    if(i[1] > maior):
        maior = i[1]

print("\n-> O número de cores usadas foram: "+ str(maior))
print("\n\n")
