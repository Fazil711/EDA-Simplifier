import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('housing.csv')
X = df['total_rooms']
y = df['median_house_value']
plt.scatter(X, y)
plt.savefig('C:/Users/OBAID/OneDrive/Desktop/MP/static/images/plot.png')