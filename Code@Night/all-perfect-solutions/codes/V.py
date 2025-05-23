# Estrutura de dados utilizada: variáveis para rastrear estado de compra/venda
# Tipo de algoritmo: varredura sequencial (linear scan) com simulação de compra/venda

N, C = map(int, input().split())
P = list(map(int, input().split()))

lucro = 0
comprado = False
preco_compra = 0

for i in range(N):
    # Comprar se não está comprado e amanhã o preço sobe o suficiente
    if not comprado and i < N-1 and P[i+1] > P[i] + C:
        comprado = True
        preco_compra = P[i] + C
    # Vender se está comprado e amanhã o preço cai ou é o último dia
    elif comprado and (i == N-1 or P[i+1] < P[i]):
        lucro += P[i] - preco_compra
        comprado = False

print(lucro)