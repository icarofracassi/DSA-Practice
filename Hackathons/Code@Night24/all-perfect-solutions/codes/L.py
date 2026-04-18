# Estrutura de dados utilizada: lista de segmentos ordenada por intervalo x, busca binária para consultas
# Tipo de algoritmo: busca binária e simulação

import sys
import bisect

input = sys.stdin.readline

N, C = map(int, input().split())
segments = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    segments.append((x1, x2, y1, y2))

# Ordena os segmentos pelo início do intervalo x
segments.sort()

# Para busca binária, vamos guardar os inícios dos intervalos
x_starts = [seg[0] for seg in segments]

def find_segment(x):
    idx = bisect.bisect_right(x_starts, x) - 1
    if idx < 0 or x > segments[idx][1]:
        return None
    return segments[idx]

def simulate(x):
    while True:
        seg = find_segment(x)
        if not seg:
            return (x,)
        x1, x2, y1, y2 = seg
        # Calcula y para o x atual
        if x1 == x2:
            y = max(y1, y2)
        else:
            y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
        if y1 == y2:
            # Segmento horizontal, balão fica preso
            return (x, int(y))
        else:
            # Segmento inclinado, balão escapa pelo ponto mais alto
            if y1 > y2:
                x, y = x1, y1
            else:
                x, y = x2, y2
            # Continua a simulação a partir do novo x
            # Mas se não houver segmento cobrindo esse x, balão escapa
            if not find_segment(x):
                return (x,)
            # Se houver, repete o processo

for _ in range(C):
    qx = int(input())
    res = simulate(qx)
    print(*res)