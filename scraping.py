# モジュールのインポート
import urllib.request as req
from bs4 import BeautifulSoup
import time

# 任意のURLからデータを取得
url = "https://su-gi-rx.com/"
res = req.urlopen(url)

