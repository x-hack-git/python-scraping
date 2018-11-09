# モジュールのインポート
import urllib.request as req
from bs4 import BeautifulSoup
import time

# スクレイピングするURLを設定
url = "https://www.amazon.co.jp/s/ref=nb_sb_noss_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&url=search-alias%3Daps&field-keywords=python"

# そのURLのオブジェクトを生成
webpage = req.urlopen(url)

# BeautifulSoupを使って解析
soup = BeautifulSoup(webpage, 'html.parser')
results_array = soup.select(".s-access-title")

titles_array = []
for result in results_array:
    title = result.string
    print(title)
    result.append(title)
