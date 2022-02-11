#%%
import pandas as pd
caseRate = pd.read_json('./covid19/totCase.json')
GDPTop10 = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Italy', 'Canada', 'South Korea']
caseRate = caseRate.loc[caseRate['date'] == '2021-12-19']
caseRate = caseRate.loc[caseRate['country'].isin(GDPTop10)]
print(caseRate)
caseRate = caseRate.set_index('country')['totCase']
caseRate.plot.box(title='case rate in GDP top 10 country', grid=True)
# %%
