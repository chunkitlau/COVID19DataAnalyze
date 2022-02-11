#%%
import pandas as pd
totCase = pd.read_json('./covid19/totCase.json')
totCaseTop =  totCase.loc[totCase['date'] == '2021-12-19'].sort_values(by=['totCase'], ascending=False).reset_index(drop=True).set_index('country')[['totCase']]
dropList = ['World', 'High income', 'Upper middle income', 'Asia', 'Europe', 'Lower middle income', 'North America', 'European Union', 'South America', 'Africa']
totCaseTop = totCaseTop.drop(dropList, axis=0).reset_index()
totCaseCount = totCaseTop.loc[0:10,:]
totCaseCount = totCaseCount.set_index('country')
totCaseCount.loc['other'] = totCaseTop.loc[10:,:].sum(axis=1)
totCaseCount.plot.pie(title='tot case pie in country', y='totCase', figsize=(5, 5))
# %%
