#%%
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
import imgkit
vaccineRate = pd.read_json('./covid19/vaccineRate.json')
print(vaccineRate)
for i in vaccineRate.index:
    vaccineRate['vaccineRate'][i] = float(vaccineRate['vaccineRate'][i].replace('%', ''))
vaccineRate = vaccineRate.sort_values(by=['vaccineRate'], ascending=False).set_index('country')
dropList = ['World', 'High income', 'Upper middle income', 'Asia', 'Europe', 'Lower middle income', 'North America', 'European Union', 'South America', 'Africa']
vaccineRate = vaccineRate.drop(dropList, axis=0)[['vaccineRate']].reset_index()

countries = list([vaccineRate['country'][i] for i in vaccineRate.index])
vaccineRates = list([vaccineRate['vaccineRate'][i] for i in vaccineRate.index])
map = Map(init_opts=opts.InitOpts(width='100%', height='1200px'))
map.add("vaccineRate", [list(z) for z in zip(countries, vaccineRates)], 'world')
map.set_global_opts(
    title_opts=opts.TitleOpts(title='World VaccineRate'), #标题
    visualmap_opts=opts.VisualMapOpts(min_=0,max_=100)) #热⼒图数值区间
map.set_series_opts(label_opts=opts.LabelOpts(is_show=True)) #热⼒图图例
map.render("map.html") #导出html
imgkit.from_file('./map.html', './map.jpg')
# %%
