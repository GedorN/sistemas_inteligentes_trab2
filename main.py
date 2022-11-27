import pandas as pd
from GraphCurve import GraphCurve
from Graph import Graph

file = pd.read_csv('./tar2_sinais_vitais_treino_com_label.txt')
file = file.reset_index() 

# Dados do gráfico fuzzy de qualidade de pressão
beginsPressure = [-10, -5, -3, 0, 3, 5]
endsPressure = [-5, -2, 0, 4, 5, 10]
relationsPressure = ["-0.04x+0.6", "-0.33x+-0.67", "0.33x+1", "-0.2x+1", "0.33x+-0.67", "0.04x+0.6"]
labelPressure = ["baixo", "baixo", "bom", "bom", "alto", "alto"]
GraphPressure = Graph("Qualidade de pressão")

# Dados do gráfico fuzzy de batimentos cardiacos
beingHeart = [0, 45, 50, 90, 90]
endHeart = [50, 50, 90, 95, 200]
relationsHeart = ["-0.02x+1", "0.2x+-9", "1", "-0.2x+19", "0.009x+-0.81"]
labelHeart = ["baixo", "bom", "bom", "bom", "alto"]
GraphHeart = Graph("Batimentos Cardíacos")

# Dados do gráfico fuzzy de respiração
beginBreathing = [0, 10, 14, 16, 18]
endBreathing = [12, 14, 16, 20, 40]
relationsBreathing = ["-0.08x+1", "0.25x+-2.5", "1", "-0.25x+5", "0.05x+-0.82"]
labelBreating = ["baixo", "bom", "bom", "bom", "alto"]
GraphBreating = Graph("Frequência Respiração")

#Dados do gráfico fuzzy de gravidade
beginsGravity = [0, 24, 25, 49, 50, 74, 75, 87]
endsGravity = [24, 26, 49, 51, 74, 76, 87, 200]
relationsGravity = ["1", "-0.5x+13", "0.0417x+-1.0433", "-0.5x+25.5", "0.0417x+-2.0858", "-0.5x+38", "0.0833x+-6.2471", "1"]
labelGravity = ["critico","critico","instavel","instavel","potencialmente_estavel","potencialmente_estavel","estavel","estavel"]
GraphGravity = Graph("Gravidade")

for i in range(0, len(beginsPressure)):
  curve = GraphCurve(beginsPressure[i], endsPressure[i], relationsPressure[i], labelPressure[i])
  GraphPressure.addCurve(curve)

for i in range(0, len(beingHeart)):
  curve = GraphCurve(beingHeart[i], endHeart[i], relationsHeart[i], labelHeart[i])
  GraphHeart.addCurve(curve)

for i in range(0, len(beginBreathing)):
  curve = GraphCurve(beginBreathing[i], endBreathing[i], relationsBreathing[i], labelBreating[i])
  GraphBreating.addCurve(curve)

for i in range(0, len(beginsGravity)):
  curve = GraphCurve(beginsGravity[i], endsGravity[i], relationsGravity[i], labelGravity[i])
  GraphGravity.addCurve(curve)

# print(file)

for index, row in file.iterrows():
  preassure = row['qPA']
  heart = row['pulso']
  breathing = row['resp']
  pertinencesValuesPressure, pertinencesLabelsPressure = GraphPressure.getPertinences(preassure)
  pertinencesValuesHeart, pertinencesLabelsheart = GraphHeart.getPertinences(heart)
  pertinencesValuesBreating, pertinencesLabelsBreating = GraphBreating.getPertinences(breathing)
  value = None

  # print(pertinencesValuesPressure)
  # print(pertinencesLabelsPressure)

  # Ifs da contrução da lógica fuzzy
  if (pertinencesValuesPressure[pertinencesLabelsPressure.index("alto")] > 0):
    indexPreassure = pertinencesLabelsPressure.index("alto")
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    indexBreating = pertinencesValuesBreating.index(min(pertinencesValuesBreating))
    preassureWeight = 6.3145
    heartWeight = -0.3817
    breathingWeigh = -1.8384
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)

  elif (pertinencesValuesHeart[pertinencesLabelsheart.index("alto")] > 0):
    indexHeart = pertinencesLabelsheart.index("alto")
    indexPreassure = pertinencesValuesPressure.index(min(pertinencesValuesPressure))
    indexBreating = pertinencesValuesBreating.index(min(pertinencesValuesBreating))
    preassureWeight = -0.688
    heartWeight = 0.032
    breathingWeigh = 1.662
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)
  elif (pertinencesValuesBreating[pertinencesLabelsBreating.index("alto")] > 0):
    indexBreating = pertinencesLabelsBreating.index("alto")
    indexPreassure = pertinencesValuesPressure.index(min(pertinencesValuesPressure))
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    preassureWeight = 0.8437
    heartWeight = 0.04512
    breathingWeigh = -0.1248
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)

  elif (pertinencesValuesPressure[pertinencesLabelsPressure.index("baixo")] > 0):
    indexPreassure = pertinencesLabelsPressure.index("baixo")
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    indexBreating = pertinencesValuesBreating.index(min(pertinencesValuesBreating))
    preassureWeight = 0.1049
    heartWeight = 0.02628
    breathingWeigh = 1.2913
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)

  elif (pertinencesValuesHeart[pertinencesLabelsheart.index("baixo")] > 0):
    indexBreating = pertinencesLabelsheart.index("baixo")
    indexPreassure = pertinencesValuesPressure.index(min(pertinencesValuesPressure))
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    preassureWeight = -0.9192
    heartWeight = -4.55749
    breathingWeigh = 21.515
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)

  elif (pertinencesValuesBreating[pertinencesLabelsBreating.index("baixo")] > 0):
    indexBreating = pertinencesLabelsBreating.index("baixo")
    indexPreassure = pertinencesValuesPressure.index(min(pertinencesValuesPressure))
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    preassureWeight = -0.0537
    heartWeight = 0.066
    breathingWeigh = 0.72595
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)
  elif (pertinencesValuesPressure[pertinencesLabelsPressure.index("bom")] > 0 and pertinencesValuesHeart[pertinencesLabelsheart.index("bom")] > 0):
    indexPreassure = pertinencesLabelsPressure.index("baixo")
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    indexBreating = pertinencesValuesBreating.index(min(pertinencesValuesBreating))
    preassureWeight = -28.0138
    heartWeight = -0.72725
    breathingWeigh = 1.94372
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)
  elif (pertinencesValuesPressure[pertinencesLabelsPressure.index("bom")] > 0 and pertinencesValuesBreating[pertinencesLabelsBreating.index("bom")] > 0):
    indexPreassure = pertinencesLabelsPressure.index("baixo")
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    indexBreating = pertinencesValuesBreating.index(min(pertinencesValuesBreating))
    preassureWeight = 24.1209
    heartWeight = -0.0172
    breathingWeigh = 0.14498
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)
  elif (pertinencesValuesHeart[pertinencesLabelsheart.index("bom")] > 0 and pertinencesValuesBreating[pertinencesLabelsBreating.index("bom")] > 0):
    indexPreassure = pertinencesLabelsPressure.index("baixo")
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    indexBreating = pertinencesValuesBreating.index(min(pertinencesValuesBreating))
    preassureWeight = 5.1865
    heartWeight = 2.837
    breathingWeigh = -16.7698
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)
  else:
    indexPreassure = pertinencesValuesPressure.index(min(pertinencesValuesPressure))
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    indexBreating = pertinencesValuesBreating.index(min(pertinencesValuesBreating))
    preassureWeight = 0.886
    heartWeight = 0.4625
    breathingWeigh = -2.387732
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)

  print(f"Linha {index} valor: {value}")

qPA = file['qPA']
pulso = file['pulso']
resp = file['resp']
grav = file['grav'] 
count = 0
for index, item in enumerate(pulso):
  pertinencesValues, pertinencesLabels = GraphHeart.getPertinences(item)
  if (True):
    pertinencesValues, pertinencesLabels = GraphPressure.getPertinences(qPA[index])
    print('---------------------------- Pressão:',qPA[index] )
    count+=1
    print(pertinencesValues)
    print(pertinencesLabels)
    print()
    print('---------------------------- pulso:', pulso[index])
    pertinencesValues, pertinencesLabels = GraphHeart.getPertinences(pulso[index])
    print(pertinencesValues)
    print(pertinencesLabels)
    print()
    print('---------------------------- resp:', resp[index])
    pertinencesValues, pertinencesLabels = GraphBreating.getPertinences(resp[index])
    print(pertinencesValues)
    print(pertinencesLabels)
    pertinencesValues, pertinencesLabels = GraphGravity.getPertinences(grav[index])
    print('---------------------------- gravidade:',grav[index] )
    print(pertinencesValues)
    print(pertinencesLabels)
    print()
    print(grav[index])
    print('##################################################################')
  if (count == 3):
    break


