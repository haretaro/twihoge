import json
from requests_oauthlib import OAuth1Session

woeids = {
        'Japan':23424856,
        'Okinawa':2345896,
        'Tokyo':1118370,
        'Worldwide':1
        }

class TwitterApi:
    def __init__(self, consumer_key, consumer_secret,
            access_token, access_token_secret):
        self.session = OAuth1Session(consumer_key,consumer_secret,
                access_token,access_token_secret)
        self.lang = 'ja'
        self.locale = 'ja'
        self.woeid = woeids['Japan']

    #フォロワーのjsonリストを返す
    def followers(self, screen_name, count=20):
        url = 'https://api.twitter.com/1.1/followers/list.json'
        params = {'screen_name':screen_name,
                'count':count}
        r = self.session.get(url,params = params)
        return r

    #フォロワーのscreen_nameを返す
    def followers_name(self, screen_name, count = 20):
        f = self.followers(screen_name,count=count)
        return [u['screen_name']for u in f.json()['users']]

    def load_json_file(filename):
        """キーを書いたjsonファイルを読んでインスタンスを返す"""
        keyfile = open(filename)
        keys = json.loads(keyfile.read())
        keyfile.close()
        return TwitterApi(keys['consumer_key'],
                keys['consumer_secret'],
                keys['access_token'],
                keys['access_token_secret'])

    def search(self,query,count=5,resulttype='recent'):
        """query:検索文字列
        count:取得するツイートの数
        resulttype:取得するツイートの種類popular|recent|mixed"""
        url = 'https://api.twitter.com/1.1/search/tweets.json'
        params = {'q':query,
                'result_type':resulttype,
                'count':count,
                'lang':self.lang,
                'locale':self.locale}
        r = self.session.get(url,params = params)
        return r

    def search_statustexts(self,query,count=5,resulttype='recent'):
        """searchメソッドの簡易版.ステータステキストのみ返却"""
        res = self.search(query,count,resulttype)
        statuses = res.json()['statuses']
        statustexts = [status['text'] for status in statuses]
        return statustexts

    def trends(self):
        """トレンドをResponseオブジェクトで返す"""
        url = 'https://api.twitter.com/1.1/trends/place.json'
        params = {'id':self.woeid}
        r = self.session.get(url,params = params)
        return r

    def trendwords(self):
        """trendsメソッドの簡易版.トレンドワードのみ返却"""
        res = self.trends()
        trends = res.json()[0]['trends']
        names = [trend['name'] for trend in trends]
        return names

    def tweet(self,statustext):
        """ツイートする"""
        url = 'https://api.twitter.com/1.1/statuses/update.json'
        params = {'status':statustext}
        r = self.session.post(url,params = params)
        return r

    #フォローしてないフォロワーを返す
    def unfollowing_followers(self, screen_name):
        followers = self.followers(screen_name, count=200)
