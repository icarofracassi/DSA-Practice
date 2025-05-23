# Estrutura de dados utilizada: lista para armazenar a pontuação de cada jogador
# Tipo de algoritmo: varredura sequencial (linear scan) e desempate pelo último a jogar

J, R = map(int, input().split())
pontos = list(map(int, input().split()))
soma = [0] * J

for i, p in enumerate(pontos):
    soma[i % J] += p

max_pontos = max(soma)
# Em caso de empate, vence o último a jogar com a pontuação máxima
for i in range(len(pontos)-1, -1, -1):
    jogador = i % J
    if soma[jogador] == max_pontos:
        print(jogador + 1)
        break