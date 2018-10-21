import twitter

api = twitter.Api(consumer_key='FILL-ME-IN',consumer_secret='FILL-ME-IN',access_token_key='FILL-ME-IN',access_token_secret='FILL-ME-IN')

print(api.VerifyCredentials())

t = api.GetUserTimeline(screen_name="akras14", count=200)

tweets = [i.AsDict() for i in t]

for t in tweets:
    print(t['id'], t['text'])
