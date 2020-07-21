from pytrends.request import TrendReq
pytrends = TrendReq(hl='ja-JP', tz=360)

# Python3 code to iterate over a list 
kw_list = ["アメリカ"]
   
# Using for loop 
# for keyword in kw_list: 
# print(keyword) 

pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='JP', gprop='')
# result = pytrends.interest_by_region(resolution='DMA', inc_low_vol=True, inc_geo_code=False)
# result = pytrends.related_topics()
date = '2020-04'
df = pytrends.related_topics()
print(df) 
# df.to_csv('data/' + 'keyword' + '.csv', encoding='utf_8')
compression_opts = dict(method='zip', archive_name='out.csv') 
df.to_csv('out.zip', index=False, compression=compression_opts)  