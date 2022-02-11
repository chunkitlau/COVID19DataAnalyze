#%%
import pandas as pd
totCase = pd.read_json('./covid19/totCase.json')
newCase = totCase.groupby('country')['totCase'].agg(['min','max'])
newCase = (newCase['max'] - newCase['min']).sort_values(ascending=False)
print(newCase)
newCase.to_csv('newCase.csv', index=True)
newCases = []
countrys = ['United States','United Kingdom','France','Germany','Russia','Poland','South Africa','Italy','Turkey','Spain']
for country in countrys:
    newCase = totCase.loc[totCase['country'] == country]
    newCase = newCase.drop(columns=['country']).set_index('date')
    newCase = newCase.loc[['2021-12-' + str(date).zfill(2) for date in range(6, 20)]].reset_index(drop=True). \
        subtract(newCase.loc[['2021-12-' + str(date).zfill(2) for date in range(5, 19)]].reset_index(drop=True))
    newCase = newCase.rename({'totCase':country}, axis=1)
    newCases.append(newCase)
df = pd.concat(newCases)
df.plot(title='new case in 10 country', marker='.', grid=True)
# %%
