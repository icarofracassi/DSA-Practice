N = int(input())
M = input().split()

values = []
far = 0
farest = 0

for id, i in enumerate(M):
    if id == N-1:
        break           # nao rodar para a ultima posicao

    far = id + int(i)
    values.append(far)
    farest = max(values)

    if id == far and farest <= id:
        break           # nao consegue mais andar para frente

    if far >= N-1:
        break           # ja chegou no final

if farest >= N-1:
    print("OK")
else:
    print("NAO")