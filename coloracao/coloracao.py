import os
import copy

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

    def calcula_e_ordena_pesos(self):
        v_peso = []
        v = 0

        #Calcula Graus
        for i in self.grafo:       
            c = 0
            for j in i:
                if(j == 1):
                    c = c + 1
            v_peso.append([c,(v + 1)])
            v = v + 1

        #Ordena vetor
        v_peso = sorted(v_peso, key=lambda x: x[0], reverse=True)

        #retorno
        return v_peso
        
    def coloracao(self):
        #variáveis
        cores = []
        var = []
        atribui_cor = []
        
        #distribuindo vetor de cores
        for i in range(0, self.vertices, 1):
            var.append(i + 1)
        
        for i in range(0, self.vertices, 1):
            cores.append(copy.copy(var))
        
        #colorindo
        pesos = self.calcula_e_ordena_pesos()

        #vetor que percorre linha
        for i in range(0, self.vertices, 1):
            v_atual = pesos[i][1]
            atribui_cor.append([v_atual, cores[v_atual - 1][0]])

            #vetor que percorre coluna
            for j in range(0, self.vertices, 1):
                x = self.grafo[v_atual - 1][j]

                #Condicao: Se haver adjascencia, irá apagar a cor da adjascencia
                if(x == 1):
                    cor_atual = cores[v_atual - 1][0]

                    for k in range(0, len(cores[j]), 1):
                        if(cores[j][k] == cor_atual):
                            cores[j].pop(k)
                            break
        
        return atribui_cor


