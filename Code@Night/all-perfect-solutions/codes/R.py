# Estrutura de dados utilizada: apenas variáveis inteiras (simulação de permutação por índices)
# Tipo de algoritmo: análise de permutação cíclica (cálculo do período do embaralhamento)

P = int(input())
pos = 1
count = 0
while True:
    if pos <= P // 2:
        pos = 2 * pos
    else:
        pos = 2 * (pos - P // 2) - 1
    count += 1
    if pos == 1:
        break
print(count)