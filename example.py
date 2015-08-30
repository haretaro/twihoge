from twihoge import TwitterApi

twitter = TwitterApi.load_json_file('keys.json')
trend = twitter.trendwords()[0]
for statustext in twitter.search_statustexts(trend):
    print(statustext)
