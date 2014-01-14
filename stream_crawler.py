from TwitterAPI import TwitterAPI

# the following credentials can be found in the app page in tchpaloalto
CONSUMER_KEY = "Oyebr7Dx5LVseGP5tsuA"
CONSUMER_SECRET = "S2X5iS7TZPhElZl1bq01LVMJ3CPxT0xbRKUEgckk"

ACCESS_KEY = "319176278-N7t6T1oRJhNlx0RMePKdkyKk0UK8BEgdpIpiw31Y"
ACCESS_SECRET = "FxbhHZ5g5ddLdGFGI4TTTlwuScFoOIVUi7FZSQBxqg4DD"

def analyze_user(api, screen_name):
    r = api.request('statuses/user_timeline',
                    {'screen_name':screen_name, 'count':200})
    tweetCount = 1
    for item in r.get_iterator():
        if 'text' in item.keys():
            print str(tweetCount) + ': ' + item['text']
            tweetCount += 1

def collect_stream(api):
    r = api.request('statuses/sample')
    tweetCount = 0
    for item in r.get_iterator():
        if 'text' in item.keys():
            tweet = item['text']
            screen_name = item['user']['screen_name']
            # Here we need to check whether a tweet is Chinese or Japanese
            if (any(u'\u4e00' <= ch <= u'\u9fff' for ch in tweet)
                and not any(u'\u3040' <= ch <= u'\u30ff' for ch in tweet)):
                print screen_name
                print tweet
                analyze_user(api, screen_name)

            tweetCount += 1
            if tweetCount % 1000 == 0:
                print tweetCount


api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET,
                 ACCESS_KEY, ACCESS_SECRET)

collect_stream(api)
