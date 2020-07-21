# GoogleTrends にアクセスするライブラリの初期化
from pytrends.request import TrendReq
pytrends = TrendReq(hl='ja-JP', tz=360)

# GoogleTrends に渡したいキーワードをセットする 
keywords = ["/m/09qlj0"]
prefs=['JP-01','JP-03','JP-04','JP-05','JP-12','JP-13','JP-14']
geos = ['JP']
    
for keyword in keywords:
    for geo in geos:
        for pref in prefs:
            # Google Trends に 取得したいデータや期間などの情報を渡す
            pytrends.build_payload([keyword], cat=0, timeframe='today 5-y', geo=pref, gprop='')

            # 取得したいデータを取り出す
            # res = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)

            data1 = pytrends.related_queries()
            print(data1[keyword]['top'])
            data1[keyword]['top'].to_csv('data/' + pref + 'top_ヒヨドリ.csv', encoding='utf_8_sig')
            # data1[keyword]['rising'].to_csv('data/' + pref + 'rising_ヒヨドリ.csv', encoding='utf_8_sig')
