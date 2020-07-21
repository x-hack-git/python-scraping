import tweepy
import json

# 注意！！
# 講義後、こちらのAPI KEYは削除し使用できなくなります
consumer_key="TMRD0LrWKtq4d5EHol82FPzRE"
consumer_secret="Oi1tkHZwPMLrAOuNsBGfh6KuafHeHAbWNyd0s2lsjV7mWflLXJ"
access_token_key="1018671407373250560-SULFtZWW0z99KEdtQtwrcmZomhVuz9"
access_token_secret="bGbb02xpH3Z6zqseYA5wsweXGKErqw0P80wg1f4rgmC8h"

# Twitterアカウントとしてログイン
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search, q="鎌倉旅行 -filter:retweets").items(100)
for tweet in tweets:
    try:
        # 画像がないツイートの際に、エラーになるので、 try - except を使用しています
        json = tweet._json
        print('-------------')
        print(json['text'])
        print(json['location'])
    except:
        pass
