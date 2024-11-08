import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, arquivo):
        self.grafo = {} 
        self.load_data(arquivo)

    def load_data(self, arquivo):
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            for linha in linhas:
                linha = linha.strip()
                if linha:
                    a, b, peso = linha.split()
                    peso = int(peso)  
                    self.add_edge(a, b, peso)

    def add_edge(self, a, b, peso):
        if a not in self.grafo:
            self.grafo[a] = {}
        if b not in self.grafo:
            self.grafo[b] = {}

        self.grafo[a][b] = peso

    def dijkstra(self, start):
        # Inicializar distâncias e predecessores
        D = {node: float('inf') for node in self.grafo}
        D[start] = 0
        predecessors = {node: None for node in self.grafo}
        N = set()

        while len(N) < len(self.grafo):
  
            w = min((node for node in self.grafo if node not in N), key=lambda node: D[node])

     
            N.add(w)

            for neighbor, cost in self.grafo[w].items():
                if neighbor not in N:
                    new_distance = D[w] + cost
                    if new_distance < D[neighbor]:
                        D[neighbor] = new_distance
                        predecessors[neighbor] = w  

        return D, predecessors

    def reconstruir_caminho(self, predecessors, start, end):
        caminho = []
        atual = end
        while atual is not None:
            caminho.append(atual)
            atual = predecessors[atual]
        caminho.reverse()
        return caminho if caminho[0] == start else None  


caminho_arquivo = 'num2.txt'
grafh = Grafo(caminho_arquivo)


start_vertex = input("Digite o vértice de início: ")
distances, predecessors = grafh.dijkstra(start_vertex)



for node in grafh.grafo:
    if node != start_vertex:
        caminho = grafh.reconstruir_caminho(predecessors, start_vertex, node)
        if caminho:
            print(f"Caminho mais curto de {start_vertex} para {node}: {' -> '.join(caminho)} com distância {distances[node]}")
        else:
            print(f"Não há caminho de {start_vertex} para {node}")
