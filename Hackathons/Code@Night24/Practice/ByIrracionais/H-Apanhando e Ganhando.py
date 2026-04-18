def transformInt(string):
    aux = []
    for i in range(0, len(string)):
        aux.append(int(string[i]))
    return aux

def transformStr(lista):
    aux = ""
    for i in lista:
        aux += str(i)
    return aux

while True:
    entradas = input().split(" ")
    if int(entradas[0]) == 0 and int(entradas[1]) == 0:
        break
    qtdDgt = int(entradas[0])
    qtdRemov = int(entradas[1])
    valor = transformInt(input())
    valorOrd = valor.copy()
    valorOrd.sort()

    for i in range(0, qtdRemov):
        valor.remove(valorOrd[0])
        valorOrd.pop(0)
    
    print(transformStr(valor))




    