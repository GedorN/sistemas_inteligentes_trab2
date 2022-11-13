import pandas as pd
from GraphCurve import GraphCurve
from Graph import Graph

file = pd.read_csv('./tar2_sinais_vitais_treino_com_label.txt')


# Dados do gráfico fuzzy de qualidade de pressão
beginsPressure = [-10, -5, -3, 0, 3, 5]
endsPressure = [-5, -2, 0, 4, 5, 10]
relationsPressure = ["-0.04x+0.6", "-0.33x+-0.67", "0.33x+1", "-0.2x+1", "0.33x+-0.67", "0.04x+0.6"]
labelPressure = ["baixo", "baixo", "bom", "bom", "alto", "alto"]
GraphPressure = Graph("Qualidade de pressão")

# Dados do gráfico fuzzy de batimentos cardiacos
beingHeart = [0, 45, 50, 90, 90]
endHeart = [50, 50, 90, 95, 200]
relationsHeart = ["-0.02x+1", "0.2x+-9", "1", "-02x+19", "0.01x+-0.82"]
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

# pertinencesValues, pertinencesLabels = GraphPressure.getPertinences(4.768427)
# print(pertinencesValues)
# print(pertinencesLabels)
# print("file",file['qPA'])
qPA = file['qPA']
pulso = file['pulso']
resp = file['resp']
grav = file['grav']
# print('---------------------------------',qPA)
count = 0
for index, item in enumerate(pulso):
  pertinencesValues, pertinencesLabels = GraphHeart.getPertinences(item)
  if (pertinencesValues[pertinencesLabels.index("alto")] > 0):
    print('---------------------------- Pressão:', item)
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
    print(grav[index])
    print('##################################################################')
  if (count == 3):
    break