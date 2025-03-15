qtd = int(input())
opParticipantes = input().split(" ")
tipoSanduiches = input().split(" ")

for i in range(qtd * qtd): 
  if len(tipoSanduiches) == 0:
    break
  else:
    if tipoSanduiches [0] == opParticipantes[0]:
      tipoSanduiches.pop(0)
      opParticipantes.pop(0)
    else:
      opParticipantes.append(opParticipantes.pop(0))


print(len(tipoSanduiches))
