# モジュールのインポート
import urllib.request as req
from bs4 import BeautifulSoup
import time
import csv

# スクレイピングするURLを設定
url = "http://www.starbucks.co.jp/beverage/"

# そのURLのオブジェクトを生成

# BeautifulSoupを使って解析
def scrape(url_array):
    for url in url_array:
        webpage = req.urlopen(url)
        soup = BeautifulSoup(webpage, 'html.parser')
        results_array = soup.select(".productName")
        print(results_array[0].string)

urls = ["http://www.starbucks.co.jp/beverage/", "http://www.starbucks.co.jp/food/"]
scrape(urls)

# with open('results.csv', 'w') as f:
#     writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく

#     for result in results_array:
#         title = result.string
#         # print(title)
#         writer.writerow([title])
