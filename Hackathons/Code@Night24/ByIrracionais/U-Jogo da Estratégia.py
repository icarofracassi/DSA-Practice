jr = input().split(" ")
nJogadores = int(jr[0])
nRodadas = int(jr[1])
pontos = input().split(" ")
maiorPontuação = 0
resposta = 0
for j in range(0, nJogadores):
    aux = 0
    for r in range(j, len(pontos), nJogadores):
        aux += int(pontos[r])
    if aux >= maiorPontuação:
        maiorPontuação = aux
        resposta = j+1
print(resposta)
