class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adicionaArestas(self, a, b, peso):
        self.grafo[a - 1].append([b, peso])

    def mostraGrafo(self):
        for i in range(self.vertices):
            print(""+ str(i + 1) +": ", end="")
            for u in self.grafo[i]:
                print(""+ str(u) + " --> ", end="")
            
            print("NULL")


grafo = Grafo(3)

grafo.adicionaArestas(1,2,6)
grafo.adicionaArestas(1,3,7)
print(grafo.grafo)

grafo.mostraGrafo()