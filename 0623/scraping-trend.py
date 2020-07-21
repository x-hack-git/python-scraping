from pytrends.request import TrendReq
pytrends = TrendReq(hl='ja-JP', tz=360)

kw_list = ["JavaScript"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='JP', gprop='')

result1 = pytrends.related_queries()
print(result1)

