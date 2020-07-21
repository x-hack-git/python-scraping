from pytrends.request import TrendReq
pytrends = TrendReq(hl='ja-JP', tz=360)

kw_list = ["Trump"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='US', gprop='')

result = pytrends.interest_over_time()
# result = pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2018, month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)
# result = pytrends.interest_by_region(resolution='DMA', inc_low_vol=True, inc_geo_code=False)
# result = pytrends.related_topics()
result.to_csv('data' + "" + '.csv', encoding='utf_8')

