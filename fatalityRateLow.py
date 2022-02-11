#%%
import pandas as pd
fatalityRate = pd.read_json('./covid19/fatalityRate.json')
for i in fatalityRate.index:
    fatalityRate['fatalityRate'][i] = float(fatalityRate['fatalityRate'][i].replace('%', ''))
fatalityRateTop =  fatalityRate.sort_values(by=['fatalityRate']).reset_index(drop=True).set_index('country')
dropList = ['World', 'High income', 'Upper middle income', 'Asia', 'Europe', 'Lower middle income', 'North America', 'European Union', 'South America', 'Africa']
fatalityRateTop = fatalityRateTop.drop(dropList, axis=0).reset_index().loc[0:10,:].set_index('country')[['fatalityRate']]
fatalityRateTop.plot.bar(title='low 10 fatality rate country', grid=True)
# %%
