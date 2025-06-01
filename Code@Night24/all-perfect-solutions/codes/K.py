# Estrutura de dados utilizada: lista de adjacência para o grafo, fila de prioridade (heap) para busca
# Tipo de algoritmo: Algoritmo de caminho máximo mínimo (Widest Path) usando Dijkstra modificado

import sys
import heapq

input = sys.stdin.readline

N, M, S = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, P = map(int, input().split())
    graph[A].append((B, P))
    graph[B].append((A, P))

queries = [tuple(map(int, input().split())) for _ in range(S)]

def widest_path(start, end):
    visited = [False] * (N+1)
    max_weight = [0] * (N+1)
    max_weight[start] = float('inf')
    heap = [(-max_weight[start], start)]
    while heap:
        w, u = heapq.heappop(heap)
        w = -w
        if visited[u]:
            continue
        visited[u] = True
        if u == end:
            return w
        for v, p in graph[u]:
            if not visited[v]:
                new_w = min(w, p)
                if new_w > max_weight[v]:
                    max_weight[v] = new_w
                    heapq.heappush(heap, (-new_w, v))
    return 0

for sede, deposito in queries:
    print(widest_path(deposito, sede))