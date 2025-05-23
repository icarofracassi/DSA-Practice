# Estrutura de dados utilizada: lista de listas (matriz) para armazenar os gols dos jogadores
# Tipo de algoritmo: varredura sequencial (linear scan) para checar se todos os valores são maiores que zero

N, M = map(int, input().split())
count = 0
for _ in range(N):
    gols = list(map(int, input().split()))
    if all(g > 0 for g in gols):
        count += 1
print(count)