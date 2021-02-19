import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('diamonds.csv')
N = len(df['x'])
c = np.random.randint(1, 3, size=N)
s = np.random.randint(10, 220, size=N)
alpha = None
fig, ax = plt.subplots()
fig.set_size_inches(15.5, 8.5)
sns.scatterplot(x='x', y='y', hue='cut', size=None, data=df)
plt.show()
fig.savefig('randomscatter.png')