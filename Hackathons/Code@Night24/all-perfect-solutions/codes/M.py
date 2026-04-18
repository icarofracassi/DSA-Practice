# Estrutura de dados utilizada: conjuntos (set) para identificar os voluntários que não retornaram
# Tipo de algoritmo: diferença de conjuntos e ordenação

N, R = map(int, input().split())
retornaram = set(map(int, input().split()))
todos = set(range(1, N+1))
nao_retornaram = sorted(todos - retornaram)

if not nao_retornaram:
    print("*")
else:
    print(' '.join(map(str, nao_retornaram)), end=' ')