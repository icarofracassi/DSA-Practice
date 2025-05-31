# Estrutura de dados utilizada: listas para armazenar as coordenadas dos membros e dos coffee-corners
# Tipo de algoritmo: busca exaustiva (brute-force) com cálculo de distância de Manhattan

N, M = map(int, input().split())
membros = [tuple(map(int, input().split())) for _ in range(N)]
cafes = [tuple(map(int, input().split())) for _ in range(M)]

menor_tempo = float('inf')
vencedor = -1

for i, (mx, my) in enumerate(membros):
    tempo = min(abs(mx - cx) + abs(my - cy) for (cx, cy) in cafes)
    if tempo < menor_tempo:
        menor_tempo = tempo
        vencedor = i + 1  # índice começa em 1 conforme o problema

print(vencedor)