import os
import uuid
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

class CassandraDB(object):

	def __init__(self):
		self.host_cassandra = os.getenv("HOST_CASSANDRA")
		self.user_cassandra = os.getenv("USER_CASSANDRA")
		self.password_cassandra = os.getenv("PASSWORD_CASSANDRA")
		self._cassandra_session = self.connect_cassandra()

	def connect_cassandra(self):
		host_list = self.host_cassandra
		auth_provider = PlainTextAuthProvider(username=self.user_cassandra, password=self.password_cassandra)
		cluster = Cluster([host_list], protocol_version=4, auth_provider=auth_provider, port=9042)
		session = cluster.connect()
		session.set_keyspace('twitter')
		return session

	def insert_tweets(self, user_id, created_at, tweet, retweetcount, location, place):
		sql_insert = f"""INSERT INTO tweets (id, created_at, tweet, user_id, retweetcount, location, place) 
		VALUES (%s, '%s', '%s', '%s', %s, '%s', '%s')""" % (uuid.uuid4(), created_at, tweet, user_id, retweetcount, location, place)
		self._cassandra_session.execute(sql_insert)
		return

	def get_tweet_id(self, tweet_id):
		sql_insert = f"select * from tweets where id = {tweet_id};"
		rows = self._cassandra_session.execute(sql_insert)
		try:
			return rows[0]
		except:
			return None

	def get_all(self):
		sql_insert = "select * from tweets;"
		rows = self._cassandra_session.execute(sql_insert)
		return rows
