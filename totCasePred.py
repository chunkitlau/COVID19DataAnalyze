#%%
import pandas as pd
import numpy as np
from sklearn import linear_model
from matplotlib import pyplot as plt 
totCase = pd.read_json('./covid19/totCase.json')
for i in totCase.index:
    totCase['date'][i] = int(str(totCase['date'][i]).split(' ')[0].split('-')[2])
totCaseWrold =  totCase.loc[totCase['country'] == 'World'].drop(columns=['country']).sort_values('date').set_index('date')
x = []
y = []
plt.figure(figsize=(15, 10))
for i in totCaseWrold.index:
    x.append(i)
    y.append(totCaseWrold['totCase'][i])
date = x.copy()
x2 = x[10:]
x = x[:10]
y2 = y[10:]
y = y[:10]
plt.grid(True)
plt.plot(date, y + y2, marker='.', label='ground true')
for a,b in zip(date, y + y2):
    plt.text(a, b+1e5, '%.3f'%(b/1e8))
x2 = [_ for _ in range(15, 20)]
model = linear_model.LinearRegression()
model.fit(np.array(x).reshape(-1, 1), y)
y3 = model.predict(np.array(x2).reshape(-1, 1))
plt.scatter(date[10:], y3, c='red', marker='x', label='predict')
for a,b in zip(date[10:], y3):
    plt.text(a, b-3e5, '%.3f'%(b/1e8))
plt.legend(loc=2)
score = model.score(np.array(x2).reshape(-1, 1), y2)
plt.title('World Cumulative Predict, Score = ' + str('%.4f'%(score*100)) + '%')
plt.show()

#totCaseWrold.plot(title='tot case in world', marker='.', grid=True)
# %%
