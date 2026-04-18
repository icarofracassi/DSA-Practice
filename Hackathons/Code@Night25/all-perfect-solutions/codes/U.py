n = int(input())
numeros = input().split()
naoTemStatus = True

for i in range(n):
    if numeros.count(numeros[i]) != 3:
        print(numeros[i])
        naoTemStatus = False

if naoTemStatus:
    print(0)