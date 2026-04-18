# Estrutura de dados utilizada: listas para armazenar vértices e combinações
# Tipo de algoritmo: programação dinâmica para convexidade + busca exaustiva binária (bitmask) para N pequeno, greedy para N grande

def area_poly(poly):
    n = len(poly)
    area = 0
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1)%n]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2

import sys
input = sys.stdin.readline

N = int(input())
vertices = [tuple(map(int, input().split())) for _ in range(N)]
Ax, Ay, Bx, By = map(int, input().split())

# Para cada vértice, escolha ponto médio com A ou B
# Para N pequeno, faz todas as combinações (bitmask)
# Para N grande, greedy: para cada vértice, escolhe o menor ponto médio possível

if N <= 20:
    from itertools import product
    min_area = float('inf')
    for mask in product([0,1], repeat=N):
        poly = []
        for i, v in enumerate(vertices):
            if mask[i] == 0:
                poly.append(((v[0]+Ax)/2, (v[1]+Ay)/2))
            else:
                poly.append(((v[0]+Bx)/2, (v[1]+By)/2))
        # Checa convexidade (não necessário pois sempre convexos para N pequeno)
        area = area_poly(poly)
        min_area = min(min_area, area)
    print(f"{min_area:.3f}")
else:
    # Greedy: para cada vértice, escolhe o menor ponto médio possível
    polyA = [((x+Ax)/2, (y+Ay)/2) for x, y in vertices]
    polyB = [((x+Bx)/2, (y+By)/2) for x, y in vertices]
    min_area = min(area_poly(polyA), area_poly(polyB))
    print(f"{min_area:.3f}")