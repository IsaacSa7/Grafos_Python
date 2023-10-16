import os
from coloracao import Grafo

#funcao para limpar
def limpar():
    os.system('clear')

#Insira a quantidade de Vértices
vertice = int(input("Insira a quantidade de vértices do seu Grafo: "))
limpar()

#Criando Grafo
grafo = Grafo(vertice)

#Inserindo arestas
arestas = int(input("Insira a quantidade de arestas: "))
limpar()

for i in range(arestas):
    a = int(input("Insira o valor do ponto de partida da " + str(i + 1)+ "ª aresta: "))
    b = int(input("Insira o valor do ponto de chegada da " + str(i + 1)+ "ª aresta: "))
    peso = 1

    grafo.adicionaAresta(a, b, peso)
    limpar()

#mostra pares de vertices e cores
saida = grafo.coloracao()

print("-> [ Vértice , Cor ] é :"+ str(saida))

#quantidade de cores
maior = 0
for i in saida:
    if(i[1] > maior):
        maior = i[1]

print("\nO número de cores usadas foram: "+ str(maior))