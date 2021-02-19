import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import mean, median

df = pd.read_csv('train.csv')
N = len(df['Age'])
fig, ax = plt.subplots()
fig.set_size_inches(15.5, 8.5)
sns.barplot(x='Pclass', y='Fare', hue='Sex', data=df, order=[1, 2, 3], estimator=mean)
#saturation, 0 to 1, dark to bright
#errcolor, confidence interval line color, default 0.26, eveything else 0 to 1
#errwidth, conf int line width 1-3 recomm
#hue_order
#capsize 
#color 
#ci=95 (0 - 100)
#n_boot, number of iterations to find confidence intervals
#orient 'v' or 'h'
plt.xlabel('Shit')
plt.ylabel('Shit')
plt.title('Shit')
plt.show()
#fig.savefig('randombar.png')