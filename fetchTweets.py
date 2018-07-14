from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import sys
import json
import analysis

consumer_key = "bOjysi6SN1aYrnEpw6hNCqbq3"
consumer_secret = "4R8ua9A898SVoaMOeI8RHRN8tf8y8TjBwPTnnF1IzqeoyKWhX1"

access_token = "2577301532-7id9KDiUWVmASBGEyxgLxLLsf82jpiQATmd1wpD"
access_token_secret = "poHX33yflMYrsnDQsrW6TJ88OGmiHyg2kJFBPT77is15b"


class TweepyListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """

    def __init__(self):
        self.name = "PersianTweepy"

    def on_data(self, data):
        tweet = json.loads(data)
        json_doc = json.dumps(tweet, ensure_ascii=False)
        outputFile.write(json_doc.encode('utf8') + '\n')
        return True

    def on_error(self, status):
        print(status)


queries = {
    "Samsung": "سامسونگ",
    "FastFood": "فست فود",
    "Hakoupian": "هاکوپیان",
    "Suit": "کت و شلوار"
}

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # if len(sys.argv) > 1 and sys.argv[1] == 'live':
    #     listener = TweepyListener()
    #     stream = Stream(auth, listener)
    #     stream.filter(track=['هات داگ'])
    # else:
    for key in queries:
        outputNumber = 18
        outputFilename = "output" + str(outputNumber) + key + ".txt"
        outputFile = open(outputFilename, "w", encoding="utf-8-sig")

        i = 0
        for tweet in tweepy.Cursor(api.search,
                                   q=queries[key],
                                   count=30000,
                                   since="2018-7-08",
                                   until="2018-7-14").items():

            text = '(' + str(i) + ')' + \
                str(tweet.created_at) + '\n' + tweet.text
            i += 1
            outputFile.write(text + '\n\n\n')

        outputFile.close()
