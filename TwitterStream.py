from tweepy.streaming import StreamListener
from tweepy.auth import OAuthHandler
from tweepy import Stream

access_token = "3349647621-WaXiP7dfAxcQbdGJ83yR3Vd8b6QiXjFCYKbIban"
access_token_secret = "IDlc0a8qmy5qHc0r4PdFDlbV7lGnFKgNfIIqX9REq8AhP"

consumer_key = "QgycFk34ibBXauJwsD9mrG4B1"
consumer_secret = "JHSm8YRvYpf0I7RBbHFGPU3M68fpNNECpNvUyh3C8HGh3pnvEo"

class StdOutListener(StreamListener):

	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':

	#twitter authentification handling:
	listener = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)

	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, listener)

	stream.filter(track=['muse'])