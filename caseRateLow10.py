#%%
import pandas as pd
caseRate = pd.read_json('./covid19/caseRate.json')
caseRateLow = caseRate.sort_values(by=['caseRate']).set_index('country')
dropList = ['World', 'High income', 'Upper middle income', 'Asia', 'Europe', 'Lower middle income', 'North America', 'European Union', 'South America', 'Africa']
caseRateLow = caseRateLow.drop(dropList, axis=0).reset_index().loc[0:10,:].set_index('country')[['caseRate']]
caseRateLow.plot.bar(title='low 10 case rate country', grid=True)
# %%
