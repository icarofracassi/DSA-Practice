# Estrutura de dados utilizada: lista para armazenar as escolhas
# Tipo de algoritmo: contagem de ocorrências (linear scan)

A, B, C = map(int, input().split())
valores = [A, B, C]
if valores.count(0) == 1:
    print("A" if A == 0 else "B" if B == 0 else "C")
elif valores.count(1) == 1:
    print("A" if A == 1 else "B" if B == 1 else "C")
else:
    print("*")