from pytrends.request import TrendReq # ライブラリの仕様を宣言
pytrends = TrendReq(hl='ja-JP', tz=360) # Googleとの接続を初期化

def hoge(keyword):
    pytrends.build_payload([keyword], cat=0, timeframe='today 5-y', geo='JP', gprop='')
    result = pytrends.related_queries()
    print(result)

contries = ["アメリカ", "フランス"] # , "ドイツ", "イギリス", "日本", "イタリア", "カナダ"]
for kw in contries:
    # print(kw)
    hoge(kw)
