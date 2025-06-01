p = int(input())
baralhoFixo = []
for i in range(0, p):
    baralhoFixo.append(i+1)
baralhoCopy = baralhoFixo.copy()
resposta = 0

def passo1(lista):
    respostaA = []
    respostaB = []
    aux = int(len(lista)/2)
    for i in range(0, aux):
        respostaA.append(lista[i])
        respostaB.append(lista[i+aux])
    return respostaA, respostaB

def passo2(listaA, listaB):
    resposta = []
    aux = len(listaA)
    for i in range(0, aux):
        resposta.append(listaB[i])
        resposta.append(listaA[i])
    return resposta

while True:
    listaA, listaB = passo1(baralhoCopy)
    baralhoCopy = passo2(listaA, listaB)
    resposta += 1
    if baralhoCopy == baralhoFixo:
        print(resposta)
        break
    