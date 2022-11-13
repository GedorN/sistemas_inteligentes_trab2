class Graph:
  def __init__(self, name):
    self.curves = []
    self.name = name
  def addCurve(self, curve):
    self.curves.append(curve)
    print(len(self.curves))
  def getPertinences(self, x):
    pertinencesValues = []
    pertinencesLabels = []
    for curve in self.curves:
      if (x > curve.begin and x <= curve.end):
        expression = curve.relation
        expression = expression.split('+')
        if (len(expression) == 1):
          pertinencesValues.append(float(expression[0]))
          pertinencesLabels.append(curve.label)
        else:
          expression[0] = expression[0].replace('x', '')
          y =  float(expression[0]) * x
          y+= float(expression[1])
          pertinencesValues.append(y)
          pertinencesLabels.append(curve.label)
      else:
        pertinencesValues.append(0)
        pertinencesLabels.append(curve.label)
    return (pertinencesValues, pertinencesLabels)