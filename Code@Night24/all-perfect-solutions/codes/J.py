# Estrutura de dados utilizada: lista para armazenar as amostras
# Tipo de algoritmo: varredura sequencial (linear scan) com comparação de vizinhos

while True:
    N = int(input())
    if N == 0:
        break
    H = list(map(int, input().split()))
    picos = 0
    for i in range(N):
        prev = H[i-1]
        curr = H[i]
        next = H[(i+1)%N]
        if (curr > prev and curr > next) or (curr < prev and curr < next):
            picos += 1
    print(picos)