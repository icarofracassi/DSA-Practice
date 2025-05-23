# Estruturas de dados utilizadas: fila (queue) para os participantes e lista (stack) para os sanduíches
# Tipo de algoritmo: simulação do processo com fila e pilha

from collections import deque

N = int(input())
fila = deque(map(int, input().split()))
pilha = list(map(int, input().split()))

tentativas = 0
while fila and pilha:
    if fila[0] == pilha[0]:
        fila.popleft()
        pilha.pop(0)
        tentativas = 0
    else:
        fila.append(fila.popleft())
        tentativas += 1
        if tentativas == len(fila):
            break  # Ninguém quer o sanduíche do topo

print(len(fila))