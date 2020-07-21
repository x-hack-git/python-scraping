# GoogleTrends にアクセスするライブラリの初期化
from pytrends.request import TrendReq
pytrends = TrendReq(hl='ja-JP', tz=360)

# GoogleTrends に渡したいキーワードをセットする 
contories = ["アメリカ", "中国", "日本", "イギリス", "ドイツ"]

for contory in contories:
    # Google Trends に 取得したいデータや期間などの情報を渡す
    pytrends.build_payload([contory], cat=0, timeframe='today 5-y', geo='JP', gprop='')

    # data1 = pytrends.related_queries()
    # data1[contory]['top'].to_csv('data/related_queries/top/' + contory + '.csv', encoding='utf_8_sig')
    # data1[contory]['rising'].to_csv('data/related_queries/raising/' + contory + '.csv', encoding='utf_8_sig')

    # data2 = pytrends.interest_over_time()
    # data2.to_csv('data/interest_over_time/' + contory + '.csv', encoding='utf_8_sig')

    data3 = pytrends.related_topics()
    data3[contory]['rising'].to_csv('data/related_topics/' + contory + '.csv', encoding='utf_8_sig')

    # data2 = pytrends.related_queries()
    # print(data2)

    # 取り出したいデータを指定して、実際に取り出す処理
    # data = pytrends.related_queries()
    # data[contory]['top'].to_csv('data/related/Py_VS_R' + contory + '.csv', encoding='utf_8_sig')
    # 結果をコンソールに出力する
    # print(result1[contory]['top'].to_json)
    # for label, content in result1[contory]['top'].items():
    #     print('label:', label)
    #     print('content:', content.to_json, sep='\n')

