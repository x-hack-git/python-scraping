# GoogleTrends にアクセスするライブラリの初期化
from pytrends.request import TrendReq
pytrends = TrendReq(hl='ja-JP', tz=360)

# GoogleTrends に渡したいキーワードをセットする 
contories = ["アメリカ", "中国", "日本"]

for contory in contories:
    # Google Trends に 取得したいデータや期間などの情報を渡す
    pytrends.build_payload([contory], cat=0, timeframe='today 5-y', geo='JP', gprop='')
    # 取り出したいデータを指定して、実際に取り出す処理
    results = pytrends.related_queries()
    
    # 結果をコンソールに出力する
    print(results)
    for result in results:
        print(result)
