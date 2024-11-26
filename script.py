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

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.grafo}
        distances[start_vertex] = 0
        visited = set()
        predecessors = {vertex: None for vertex in self.grafo}

        while len(visited) < len(self.grafo):
            min_distance_vertex = None
            min_distance = float('inf')
            for vertex in distances:
                if vertex not in visited and distances[vertex] < min_distance:
                    min_distance = distances[vertex]
                    min_distance_vertex = vertex

            if min_distance_vertex is None:
                break

            visited.add(min_distance_vertex)

            for neighbor, weight in self.grafo[min_distance_vertex].items():
                if neighbor not in visited:
                    new_distance = distances[min_distance_vertex] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = min_distance_vertex

        return distances, predecessors

    def print_paths(self, start_vertex):
        distances, predecessors = self.dijkstra(start_vertex)

        for vertex in self.grafo:
            if  distances[vertex] == 0:
                continue
            path = []
            current = vertex
            while current is not None:
                path.insert(0, current)
                current = predecessors[current]
            print(f"Shortest path from {start_vertex} to {vertex} (distance {distances[vertex]}): {' -> '.join(path)}")

caminho_arquivo = 'num.txt'
grafh = Grafo(caminho_arquivo)

start_vertex = input("Enter the starting vertex: ")
grafh.print_paths(start_vertex)