# モジュールのインポート
import urllib.request as req
from bs4 import BeautifulSoup
# import time

# スクレイピングするURLを設定
url = "https://www.amazon.co.jp/s/ref=nb_sb_noss_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&url=search-alias%3Daps&field-keywords=python"

# そのURLのオブジェクトを生成
webpage = req.urlopen(url)
print(webpage)

# BeautifulSoupを使って解析
soup = BeautifulSoup(webpage, 'html.parser')
result = soup.find("img").select(".hogehoge-class")

# 結果を標準出力に出力
print(result)
