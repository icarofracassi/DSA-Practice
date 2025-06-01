nRodadas = int(input())
resultado = []
for i in range(0, nRodadas):
    nCestas = int(input())
    valores = input().split(" ")
    pastelPremiado = input()
    resultado.append(str(valores.index(pastelPremiado)+1))

print (" ".join(resultado[::-1]))