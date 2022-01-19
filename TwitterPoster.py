import tweepy
from env import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class TwitterPoster:
    def post(self, text):

        client = tweepy.Client(consumer_key=API_KEY,
                            consumer_secret=API_KEY_SECRET,
                            access_token=ACCESS_TOKEN,
                            access_token_secret=ACCESS_TOKEN_SECRET
        )

        response = client.create_tweet(text=text)
        print(response)