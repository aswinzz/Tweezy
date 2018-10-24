
import tweepy

access_token = '1053705516357083136-czN4zFt29SXJxgwgzQiLXpnCnYGpjS'
access_token_secret = 'poYFeGPqAzTr7yF47geTVecSN6dYH1aeOuXdONEr8CeDk'

consumer_key = "eoWSW9nGuDnuetWn5DuRbV1Xp"
consumer_secret = "JuaBKJa0oYuZFzQe3cv4Ajuq4d7wfoD9RboBeF3otA28UOgbGj"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if __name__ == "__main__":

    ids = []
    for page in tweepy.Cursor(api.followers_ids, screen_name="aswinvb1").pages():
        ids.extend(page)

    print(len(ids))
