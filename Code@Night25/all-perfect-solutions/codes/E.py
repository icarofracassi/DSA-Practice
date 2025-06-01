n = int(input())
counter = 0
listapokedex = []

for i in range(n):
    pokename = input()
    if pokename not in listapokedex:
        listapokedex.append(pokename)
        counter += 1

nfaltam = 151 - counter
print("Falta(m) " + str(nfaltam) + " pomekon(s).")
