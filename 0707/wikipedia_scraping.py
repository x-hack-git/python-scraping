import requests

base_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top-by-country/ja.wikipedia.org"
headers = {"User-Agent": "smatsuda@x-hack.jp"}
body = {"": "twitter-api-key"}

# keywords = ['機械学習', '深層学習', 'ニューラルネットワーク']
# project = "ja.wikipedia.org"

for keyword in ['機械学習','深層学習']:
    url = base_url + "/all-access/2020/05"
    print(url)
    result = requests.get(url, body=body, headers=headers)
    print(result)
    jsonFile = result.json()
    print(jsonFile)
    # for item in jsonFile["items"]:
    #     print(item["article"], item["views"])

# url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/ja.wikipedia.org/all-access/all-agents/自然言語処理/daily/20200601/20200630"
# result = requests.get(url, headers=headers)
# print(result.json())