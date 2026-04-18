# Estrutura de dados utilizada: pilha (stack)
# Tipo de algoritmo: algoritmo guloso (greedy) com pilha para remoção de dígitos

while True:
    line = input().strip()
    if line == "0 0":
        break
    N, D = map(int, line.split())
    num = input().strip()
    stack = []
    to_remove = D
    for digit in num:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    # Se ainda restam dígitos para remover, remova do final
    result = ''.join(stack[:N-D])
    print(result)