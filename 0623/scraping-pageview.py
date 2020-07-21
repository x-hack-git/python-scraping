import requests
import csv 

url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/ja.wikipedia.org/all-access/all-agents/%E9%AC%BC%E6%BB%85%E3%81%AE%E5%88%83/daily/20200601/20200630"
headers = {"User-Agent": "smatsuda@x-hack.jp"}

r = requests.get(url, headers=headers)

data_file = open('data_file.csv', 'w')
csv_writer = csv.writer(data_file)

for item in r.json()["items"]:
    csv_writer.writerow([item["article"], item["views"]]) 