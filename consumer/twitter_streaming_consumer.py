import os
import json

from kafka import KafkaConsumer
from BD.cassandra import CassandraDB


class StorageTwitter:

	def __init__(self):
		self.topic_name = os.getenv("KAFKA_TOPIC")
		self.boostrap_host = os.getenv("BOOSTRAP_HOST")

		self._cassandra = CassandraDB()
		self._consumer = self.get_consumer_kafka()

	def get_consumer_kafka(self):
		consumer = KafkaConsumer(
			self.topic_name,
			bootstrap_servers=[self.boostrap_host],
			auto_offset_reset='latest',
			enable_auto_commit=True,
			auto_commit_interval_ms=5000,
			fetch_max_bytes=128,
			max_poll_records=100,
			value_deserializer=lambda x: json.loads(x.decode('utf-8'))
		)
		return consumer

	def start(self):
		consumer = self.get_consumer_kafka()
		for message in consumer:
			tweets = json.loads(json.dumps(message.value))
			user_id = tweets['user']['id_str']
			created_at = tweets['created_at']
			try:
				tweet = tweets['extended_tweet']['full_text']
			except:
				tweet = tweets['text']
			retweetcount = tweets['retweet_count']
			if tweets['place'] is not None:
				place = tweets['place']['country']
			else:
				place = None
			location = tweets['user']['location']

			# Store them in the Cassandra table
			self._cassandra.insert_tweets(user_id=user_id,created_at=created_at, tweet=tweet, retweetcount=retweetcount,
										  location=location, place=place)

if __name__ == "__main__":
	print("Inicializando Consumer!!!")
	ST = StorageTwitter()
	ST.start()

