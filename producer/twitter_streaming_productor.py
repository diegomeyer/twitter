import os
from time import sleep

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer

boostrap_host = os.getenv("BOOSTRAP_HOST")
topic_name = os.getenv("KAFKA_TOPIC")

producer = KafkaProducer(bootstrap_servers=boostrap_host)


class TwitterAuth():
    def __init__(self):
        self.access_token = os.getenv("ACCESS_KEY")
        self.access_token_secret = os.getenv("ACCESS_SECRET")
        self.consumer_key = os.getenv("CONSUMER_KEY")
        self.consumer_secret = os.getenv("CONSUMER_SECRET")

    def authenticateTwitterApp(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return auth


class ListenerTweetSreamer(StreamListener):
    def on_data(self, raw_data):
        producer.send(topic_name, str.encode(raw_data))
        return True

class TwitterStreamer():
    """SET UP STREAMER"""
    def __init__(self):
        self.twitterAuth = TwitterAuth()

    def on_status(self, status):
        print(status.text)

    def stream_tweets(self):
        while True:
            listener = ListenerTweetSreamer()
            auth = self.twitterAuth.authenticateTwitterApp()
            stream = Stream(auth, listener)
            stream.filter(track=["#Santander"], is_async=True)
            sleep(1)

if __name__ == "__main__":
    print("Inicializando Productor!!!")
    TS = TwitterStreamer()
    TS.stream_tweets()
