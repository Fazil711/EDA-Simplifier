import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv, io

graph = BarPlotModel.objects.get(name= 'Bar Plot')
print(graph.name)