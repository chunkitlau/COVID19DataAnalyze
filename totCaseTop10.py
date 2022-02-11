#%%
import pandas as pd
totCase = pd.read_json('./covid19/totCase.json')
totCaseTop =  totCase.loc[totCase['date'] == '2021-12-19'].sort_values(by=['totCase'], ascending=False).reset_index(drop=True)
print(totCaseTop)
totCaseTop.to_csv('totCaseTop10.csv', index=True)
Top10Country = ["United States","India","Brazil","United Kingdom","Russia","Turkey","France","Germany","Iran","Spain"]
totCaseTop10 = totCaseTop.loc[totCaseTop['country'].isin(Top10Country)]
totCaseTop10 = totCaseTop10.set_index('country')[['totCase']]
print(totCaseTop10)
totCaseTop10.plot.bar(title='top 10 tot case country', grid=True)
# %%
