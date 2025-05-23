# Estrutura de dados utilizada: lista para programação dinâmica (DP)
# Tipo de algoritmo: Programação Dinâmica (Dynamic Programming)

N = int(input())
C = list(map(int, input().split()))

dp = [0] * N
dp[0] = C[0]
dp[1] = C[1]

for i in range(2, N):
    dp[i] = C[i] + min(dp[i-1], dp[i-2])

print(min(dp[N-1], dp[N-2]))