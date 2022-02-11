#%%
import pandas as pd
totCase = pd.read_json('./covid19/totCase.json')
totCaseWrold =  totCase.loc[totCase['country'] == 'World'].drop(columns=['country']).set_index('date')
print(totCase)
print(totCaseWrold)
totCaseWrold.plot(title='tot case in world', marker='.', grid=True)
# %%
