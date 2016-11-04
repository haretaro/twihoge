from twihoge import TwitterApi

#トレンドワードから1つ選んで検索し,結果を表示するデモ
twitter = TwitterApi.load_json_file('keys.json')
trend = twitter.trendwords()[0]
print('trend word = {}'.format(trend))
for statustext in twitter.search_statustexts(trend, count=20):
    print(statustext)
