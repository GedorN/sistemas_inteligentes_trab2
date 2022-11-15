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
relationsHeart = ["-0.02x+1", "0.2x+-9", "1", "-02x+19", "0.009x+-0.81"]
labelHeart = ["baixo", "bom", "bom", "bom", "alto"]
GraphHeart = Graph("Batimentos Cardíacos")

# Dados do gráfico fuzzy de respiração
beginBreathing = [0, 10, 14, 16, 18]
endBreathing = [12, 14, 16, 20, 40]
relationsBreathing = ["-0.08x+1", "0.25x+-2.5", "1", "-0.25x+5", "0.05x+-0.82"]
labelBreating = ["baixo", "bom", "bom", "bom", "alto"]
GraphBreating = Graph("Frequência Respiração")

for i in range(0, len(beginsPressure)):
  curve = GraphCurve(beginsPressure[i], endsPressure[i], relationsPressure[i], labelPressure[i])
  GraphPressure.addCurve(curve)

for i in range(0, len(beingHeart)):
  curve = GraphCurve(beingHeart[i], endHeart[i], relationsHeart[i], labelHeart[i])
  GraphHeart.addCurve(curve)

for i in range(0, len(beginBreathing)):
  curve = GraphCurve(beginBreathing[i], endBreathing[i], relationsBreathing[i], labelBreating[i])
  GraphBreating.addCurve(curve)

print(file)

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
    preassureWeight = 219.36
    heartWeight = -14.038
    breathingWeigh = -56.99
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)

  elif (pertinencesValuesHeart[pertinencesLabelsheart.index("alto")] > 0):
    indexHeart = pertinencesLabelsheart.index("alto")
    indexPreassure = pertinencesValuesPressure.index(min(pertinencesValuesPressure))
    indexBreating = pertinencesValuesBreating.index(min(pertinencesValuesBreating))
    preassureWeight = 0
    heartWeight = -0.14
    breathingWeigh = 10.26
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)


  elif (pertinencesValuesBreating[pertinencesLabelsBreating.index("alto")] > 0):
    indexBreating = pertinencesLabelsBreating.index("alto")
    indexPreassure = pertinencesValuesPressure.index(min(pertinencesValuesPressure))
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    preassureWeight = 2.92
    heartWeight = 0.289
    breathingWeigh = -0.87
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)

  elif (pertinencesValuesPressure[pertinencesLabelsPressure.index("baixo")] > 0):
    indexPreassure = pertinencesLabelsPressure.index("baixo")
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    indexBreating = pertinencesValuesBreating.index(min(pertinencesValuesBreating))
    preassureWeight = -1.189
    heartWeight = 0.19
    breathingWeigh = 2.21
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)

  elif (pertinencesValuesHeart[pertinencesLabelsheart.index("baixo")] > 0):
    indexBreating = pertinencesLabelsheart.index("baixo")
    indexPreassure = pertinencesValuesPressure.index(min(pertinencesValuesPressure))
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    preassureWeight = 4.102
    heartWeight = 23.64552
    breathingWeigh = -101.22
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)

  elif (pertinencesValuesBreating[pertinencesLabelsBreating.index("baixo")] > 0):
    indexBreating = pertinencesLabelsBreating.index("baixo")
    indexPreassure = pertinencesValuesPressure.index(min(pertinencesValuesPressure))
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    preassureWeight = -0.279
    heartWeight = 0.332
    breathingWeigh = 3.648
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)
  else:
    indexPreassure = pertinencesValuesPressure.index(min(pertinencesValuesPressure))
    indexHeart = pertinencesValuesHeart.index(min(pertinencesValuesHeart))
    indexBreating = pertinencesValuesBreating.index(min(pertinencesValuesBreating))
    preassureWeight = 1
    heartWeight = 1
    breathingWeigh = 1
    value = (preassure * pertinencesValuesPressure[indexPreassure] * preassureWeight) + ( heart * pertinencesValuesHeart[indexHeart] * heartWeight) + (breathing * pertinencesValuesBreating[indexBreating] * breathingWeigh)
  
  print(f"Linha {index} valor: {value}")


