#%%
import pandas as pd
caseRate = pd.read_json('./covid19/caseRate.json')
caseRateTop = caseRate.sort_values(by=['caseRate'], ascending=False).set_index('country')
print(caseRateTop)
dropList = ['World', 'High income', 'Upper middle income', 'Asia', 'Europe', 'Lower middle income', 'North America', 'European Union', 'South America', 'Africa']
caseRateTop = caseRateTop.drop(dropList, axis=0).reset_index().loc[0:10,:].set_index('country')[['caseRate']]
caseRateTop.plot.bar(title='top 10 case rate country', grid=True)
# %%
