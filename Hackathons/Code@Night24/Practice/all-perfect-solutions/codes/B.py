# Estrutura de dados utilizada: lista de arestas e estrutura de união-busca (Union-Find)
# Tipo de algoritmo: Algoritmo de Kruskal para Árvore Geradora Mínima (MST)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot == yroot:
        return False
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        if rank[xroot] == rank[yroot]:
            rank[xroot] += 1
    return True

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a-1, b-1))

edges.sort()
parent = [i for i in range(N)]
rank = [0] * N
cost = 0
for c, a, b in edges:
    if union(parent, rank, a, b):
        cost += c

print(cost)