# Estrutura de dados utilizada: dicionário para memoização (programação dinâmica)
# Tipo de algoritmo: Programação dinâmica recursiva com memoização

def prob_vitoria(ev1, ev2, at, d, memo):
    if ev1 <= 0:
        return 0.0
    if ev2 <= 0:
        return 1.0
    key = (ev1, ev2)
    if key in memo:
        return memo[key]
    p1 = at / 6.0
    p2 = 1 - p1
    # Vampiro 1 vence o turno
    win1 = prob_vitoria(ev1 + d, ev2 - d, at, d, memo)
    # Vampiro 2 vence o turno
    win2 = prob_vitoria(ev1 - d, ev2 + d, at, d, memo)
    memo[key] = p1 * win1 + p2 * win2
    return memo[key]

while True:
    line = input().strip()
    if line == "0 0 0 0":
        break
    EV1, EV2, AT, D = map(int, line.split())
    memo = {}
    prob = prob_vitoria(EV1, EV2, AT, D, memo)
    print(f"{prob * 100:.1f}")