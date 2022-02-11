#%%
import pandas as pd
vaccineRate = pd.read_json('./covid19/vaccineRate.json')
print(vaccineRate)
for i in vaccineRate.index:
    vaccineRate['vaccineRate'][i] = float(vaccineRate['vaccineRate'][i].replace('%', ''))
vaccineRateLow = vaccineRate.sort_values(by=['vaccineRate'], ascending=False).set_index('country')
dropList = ['World', 'High income', 'Upper middle income', 'Asia', 'Europe', 'Lower middle income', 'North America', 'European Union', 'South America', 'Africa']
vaccineRateLow = vaccineRateLow.drop(dropList, axis=0).reset_index().loc[0:10,:].set_index('country')[['vaccineRate']]
vaccineRateLow.plot.bar(title='top 10 vaccine rate country', grid=True)
# %%
