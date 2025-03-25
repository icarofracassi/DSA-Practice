qtdColegas = int(input())
respBoolean = True

def getDatas():
  listaDiasMes = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334}
  dataIntervalo = input().split(" ")
  diaInicio, mesInicio = int(dataIntervalo[0].split("-")[0]), int(dataIntervalo[0].split("-")[1])
  diaFinal, mesFinal = int(dataIntervalo[1].split("-")[0]), int(dataIntervalo[1].split("-")[1])
  dataInicioColega = listaDiasMes[mesInicio-1] + diaInicio
  dataFinalColega = listaDiasMes[mesFinal-1] + diaFinal
  return [dataInicioColega, dataFinalColega]

if qtdColegas == 0:
  print("Sim")
else:
  datasColegas = []

  for i in range(0, qtdColegas):
      datasColegas.append(getDatas())
  datasFuncionario = getDatas()

  for j in datasColegas:
    if datasFuncionario[0] in range(j[0], j[1]+1) or datasFuncionario[1] in range(j[0], j[1]+1:
      respBoolean = False
      break
  if respBoolean: 
    print ("Sim")
  else:
    print("Nao")
