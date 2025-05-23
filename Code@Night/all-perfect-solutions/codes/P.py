# Estrutura de dados utilizada: apenas variáveis inteiras (simples)
# Tipo de algoritmo: simulação matemática (cálculo direto)

X, Y = map(int, input().split())
# O líder ultrapassa o último quando k*X >= (k-1)*Y + 1
# Procuramos o menor k tal que k*X > (k-1)*Y
k = (Y - 1) // (Y - X) + 1
print(k)