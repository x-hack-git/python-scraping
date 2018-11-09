# モジュールのインポート
import urllib.request as req
from bs4 import BeautifulSoup
import time
import csv

# スクレイピングするURLを設定
url = "https://www.amazon.co.jp/s/ref=nb_sb_noss_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&url=search-alias%3Daps&field-keywords=python"

# そのURLのオブジェクトを生成
webpage = req.urlopen(url)

# BeautifulSoupを使って解析
soup = BeautifulSoup(webpage, 'html.parser')
results_array = soup.select(".s-access-title")

with open('results.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく

    for result in results_array:
        title = result.string
        print(title)
        writer.writerow([title])
