
from heapq import heappop, heappush
from math import inf, isfinite

LOCAIS = {
    'A': 'Depósito', 'B': 'Cruzamento B', 'C': 'Cruzamento C',
    'D': 'Cruzamento D', 'E': 'Cruzamento E', 'F': 'Cruzamento F',
    'G': 'Cliente',
}
RUAS = [
    ('A', 'B', 4), ('A', 'D', 2), ('A', 'E', 7),
    ('B', 'C', 3), ('B', 'D', 1), ('C', 'D', 6),
    ('C', 'G', 5), ('D', 'E', 4), ('D', 'F', 2),
    ('D', 'G', 3), ('E', 'F', 3), ('F', 'G', 2),
]


def criar_grafo(ruas=None):
    grafo = {vertice: {} for vertice in LOCAIS}
    for origem, destino, peso in RUAS if ruas is None else ruas:
        if origem not in grafo or destino not in grafo:
            raise ValueError('Rua com vértice desconhecido.')
        if not isfinite(peso) or peso < 0:
            raise ValueError('Dijkstra exige pesos finitos e não negativos.')
        grafo[origem][destino] = peso
        grafo[destino][origem] = peso
    return grafo


def reconstruir_caminho(predecessores, origem, destino):
    caminho = []
    atual = destino
    visitados = set()
    while atual is not None:
        if atual in visitados:
            raise ValueError('Ciclo inválido na cadeia de predecessores.')
        visitados.add(atual)
        caminho.append(atual)
        if atual == origem:
            return list(reversed(caminho))
        atual = predecessores.get(atual)
    return []


def dijkstra(grafo, origem, destino):
    if origem not in grafo or destino not in grafo:
        raise ValueError('Origem ou destino inexistente.')
    for vizinhos in grafo.values():
        for vertice, peso in vizinhos.items():
            if vertice not in grafo or not isfinite(peso) or peso < 0:
                raise ValueError('Grafo inválido: vértice ou peso não permitido.')
    distancias = {vertice: inf for vertice in grafo}
    predecessores = {vertice: None for vertice in grafo}
    distancias[origem] = 0
    fila = [(0, origem)]
    while fila:
        distancia_atual, atual = heappop(fila)
        if distancia_atual != distancias[atual]:
            continue
        for vizinho, peso in grafo[atual].items():
            candidata = distancia_atual + peso
            if candidata < distancias[vizinho]:
                distancias[vizinho] = candidata
                predecessores[vizinho] = atual
                heappush(fila, (candidata, vizinho))
    if distancias[destino] == inf:
        return inf, []
    return distancias[destino], reconstruir_caminho(predecessores, origem, destino)
