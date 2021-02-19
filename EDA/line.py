import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('train.csv')
N = len(df['Age'])
alpha = 0.5
fig, ax = plt.subplots()
fig.set_size_inches(15.5, 8.5)
sns.lineplot(x='Age', y='Fare', hue='Sex', size=None, data=df, alpha=alpha)
#Style one dashed one normal
#Size of lines, can be numerical or categorical
plt.xlabel('Shit')
plt.ylabel('Shit')
plt.title('Shit')
plt.show()
fig.savefig('randomline.png')