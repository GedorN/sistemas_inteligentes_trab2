class Graph:
  def __init__(self, name):
    self.curves = []
    self.name = name
  def addCurve(self, curve):
    self.curves.append(curve)
  def getPertinences(self, x):
    pertinencesValues = []
    pertinencesLabels = []
    # Create unique array
    for curve in self.curves:
      if curve.label not in pertinencesLabels:
        pertinencesLabels.append(curve.label)
        pertinencesValues.append(0)
    for curve in self.curves:
      if (x > curve.begin and x <= curve.end):
        expression = curve.relation
        expression = expression.split('+')
        if (len(expression) == 1):
          pertinencesValues[pertinencesLabels.index(curve.label)] = (float(expression[0]))
        else:
          expression[0] = expression[0].replace('x', '')

          y =  float(expression[0]) * x
          y+= float(expression[1])
          pertinencesValues[pertinencesLabels.index(curve.label)] = y
    return (pertinencesValues, pertinencesLabels)