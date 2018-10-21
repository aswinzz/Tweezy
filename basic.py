import tweepy

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "eoWSW9nGuDnuetWn5DuRbV1Xp"
consumer_secret = "JuaBKJa0oYuZFzQe3cv4Ajuq4d7wfoD9RboBeF3otA28UOgbGj"
access_key = "1053705516357083136-czN4zFt29SXJxgwgzQiLXpnCnYGpjS"
access_secret = "poYFeGPqAzTr7yF47geTVecSN6dYH1aeOuXdONEr8CeDk"

# Function to extract tweets
def get_tweets(username):

        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)

        # Calling api
        api = tweepy.API(auth)

        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)

        # Empty Array
        tmp=[]

        # create array of tweet information: username,
        # tweet id, date/time, text
        for i in tweets:
            print(i)
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
        for j in tweets_for_csv:

            # Appending tweets to the empty array tmp
            tmp.append(j)

        # Printing the tweets
        print(tmp)


# Driver code
if __name__ == '__main__':

    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("aswinvb1")
