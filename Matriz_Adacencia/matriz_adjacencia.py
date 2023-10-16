'''
->Matriz de Adjacencia
->Grafo direcionado Simples
'''

import os
#Classe do Grafo
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adicionaAresta(self, a, b, peso):
        self.grafo[a-1][b-1] = peso
        self.grafo[b-1][a-1] = peso

    def mostraMatriz(self):
        #variaveis
        x = [0] * self.vertices
        valor = 1
        saida = "   |"

        #loops para eibir dados
        for i in range(self.vertices):
            saida = saida + str(x[i] + valor) + "| "
            valor = valor + 1
        print(saida)
        for i in range(self.vertices):
            print(str(i + 1) + " |" + str(self.grafo[i]))

#Execução principal =====================================================================

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
    peso = int(input("Insira o valor do peso da " + str(i + 1)+ "ª aresta: "))

    grafo.adicionaAresta(a, b, peso)
    limpar()

#mostrar matriz
grafo.mostraMatriz()
