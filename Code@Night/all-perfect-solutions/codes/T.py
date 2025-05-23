# Estrutura de dados utilizada: lista para armazenar fatoriais
# Tipo de algoritmo: algoritmo guloso (greedy)

N = int(input())
# Pré-calcula todos os fatoriais menores ou iguais a N
fats = []
f = 1
i = 1
while f <= N:
    fats.append(f)
    i += 1
    f *= i

count = 0
i = len(fats) - 1
while N > 0:
    if fats[i] <= N:
        N -= fats[i]
        count += 1
    else:
        i -= 1
print(count)