# GoogleTrends にアクセスするライブラリの初期化
import datetime
from pytrends.request import TrendReq
pytrends = TrendReq(hl='ja-JP', tz=360)

# GoogleTrends に渡したいキーワードをセットする 
keywords = ["/m/09qlj0"]

# 日本の場合はJP-XX (XXは01-47の都道府県コードが入ります)
prefs=['JP-01','JP-03','JP-04','JP-05','JP-12','JP-13','JP-14']
    
for keyword in keywords: # ["/m/09qlj0"]
    for pref in prefs: # ['JP-01','JP-03','JP-04','JP-05','JP-12','JP-13','JP-14']
    # Google Trends に 取得したいデータや期間などの情報を渡す
        pytrends.build_payload([keyword], cat=0, timeframe='today 5-y', geo=pref, gprop='')

        # 結果がない時の回避方法を次回
        data1 = pytrends.related_queries()
        print(data1)
        if not data1[keyword]['top'] is None:
            data1[keyword]['top'].to_csv('data/' + pref + 'top_ヒヨドリ.csv', encoding='utf_8_sig')
        if not data1[keyword]['rising'] is None:
            data1[keyword]['rising'].to_csv('data/' + pref + 'rising_ヒヨドリ.csv', encoding='utf_8_sig')