# Estrutura de dados utilizada: listas para representar permutações de linhas e colunas
# Tipo de algoritmo: análise de permutação e contagem de ciclos (perm cycles)

def count_cycles(perm):
    visited = [False] * len(perm)
    cycles = 0
    for i in range(len(perm)):
        if not visited[i]:
            cycles += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = perm[j]
    return len(perm) - cycles

L, C = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(L)]

# Calcula permutação de linhas
row_perm = []
for i in range(L):
    # O primeiro elemento da linha i deveria ser (i * C + 1)
    val = mat[i][0]
    correct_row = (val - 1) // C
    row_perm.append(correct_row)

# Calcula permutação de colunas
col_perm = []
for j in range(C):
    # O elemento da primeira linha, coluna j, deveria ser (j + 1)
    val = mat[0][j]
    correct_col = (val - 1) % C
    col_perm.append(correct_col)

# Verifica se a matriz pode ser obtida apenas trocando linhas e colunas
possible = True
for i in range(L):
    for j in range(C):
        expected = row_perm[i] * C + col_perm[j] + 1
        if mat[i][j] != expected:
            possible = False
            break
    if not possible:
        break

if not possible:
    print("*")
else:
    print(count_cycles(row_perm) + count_cycles(col_perm))