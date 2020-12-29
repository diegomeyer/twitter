from fastapi import FastAPI

from BD.cassandra import CassandraDB

app = FastAPI()
cassandra = CassandraDB()

@app.get("/")
def read_root():
    return "Urls existentes: \n" \
           "/tweet/{tweet_id} \n" \
           "/tweet"

@app.get("/tweet/{tweet_id}")
def read_item(tweet_id: str):
    data = cassandra.get_tweet_id(tweet_id=tweet_id)
    result = {
        'user_id': data.user_id,
        'created_at': data.created_at,
        'retweetcount': data.retweetcount,
        'text': data.tweet
    }
    return result

@app.get("/tweet")
def read_all_item():
    tweets = cassandra.get_all()
    result = list()
    for tweet in tweets:
        result.append({
            'user_id': tweet.user_id,
            'created_at': tweet.created_at,
            'retweetcount': tweet.retweetcount,
            'text': tweet.tweet
        })
    return result

