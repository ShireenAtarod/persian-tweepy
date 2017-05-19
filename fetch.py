from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key="bOjysi6SN1aYrnEpw6hNCqbq3"
consumer_secret="4R8ua9A898SVoaMOeI8RHRN8tf8y8TjBwPTnnF1IzqeoyKWhX1"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2577301532-7id9KDiUWVmASBGEyxgLxLLsf82jpiQATmd1wpD"
access_token_secret="poHX33yflMYrsnDQsrW6TJ88OGmiHyg2kJFBPT77is15b"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def __init__(self, filename="output.json"):
        self.outputFile = open(filename, "w")

    def on_data(self, data):
        self.outputFile.write(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['دانشگاه'])
