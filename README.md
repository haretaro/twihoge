# twihoge
pythonでtwitterを使うライブラリ
# つかいかた

jsonファイルにキーを書いておく

    {
    "consumer_key" : "qwertyqwerty",
    "consumer_secret" : "qwertyqwerty",
    "access_token" : "qwertyqwerty",
    "access_token_secret" : "qwertyqwerty"
    }

jsonファイルからキーを読んでツイートする

    from twihoge import TwitterApi
    twitter = TwitterApi.load_json_file('keys.json')
    twitter.tweet('こんにちは世界')

トレンドワードを取得する

    trendwords = twitter.trendwords()

ツイートを検索する

    searched_tweets = twitter.search_statustexts('人狼')
