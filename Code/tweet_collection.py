import twitter, sys, json
import time

reload(sys)

sys.setdefaultencoding("utf-8")

myApi = twitter.Api(consumer_key='DxWV0Jimx0VMpB9eEJreBlcb8',
                    consumer_secret='q10JExT4pch13b95ir64KD84ojAOywEMKcxuBzDmcTTh6uVw04',
                    access_token_key='4220116812-F5iMoCKRkWCt4hFdJaZ96N59gDtg1UCJtCwJWRW',
                    access_token_secret='0YRtBkDknEkwrsducXv45gxXXq0oANKnElHGhCCclqbad')

def print_info(tweet):
    print "//===========//"
    print "Tweet ID: ", tweet['id']
    print "Post Time: ", tweet['created_at']
    print "User Name: ", tweet['user']['screen_name']
    try:
        print "Tweet Text: ", tweet['text']
    except:
        pass


def query_reliance():
    query = 'RCOM OR RELCAPITAL OR "RELIANCE JIO" OR "Reliance Industries" OR RELINFRA OR RPOWER OR RELBANK OR RDEL OR RELGOLD OR RELMEDIA'

    for it in range(1):
        tweets = [json.loads(str(raw_tweet)) for raw_tweet
                  in myApi.GetSearch(term=query, count=200, since="2018-03-19", until="2018-04-17")]

        f = open('tweets_reliance.txt', 'w')
        for tweet in tweets:
            print_info(tweet)
            f.write(json.dumps(tweet['created_at'] + tweet['user']['screen_name'] + ' !!!! ' + tweet['text']) + '\n')


def query_bajaj():
    query = 'BAJAJ-AUTO OR BAJFINANCE OR "BAJAJ AUTO LIMITED" OR "BAJAJ FINANCE LIMITED" OR BAJAJCORP OR BAJAJELEC OR BAJAJFINSV OR BAJAJHIND OR BAJAJHLDNG'

    for it in range(1):
        tweets = [json.loads(str(raw_tweet)) for raw_tweet
                  in myApi.GetSearch(term=query, count=200, since="2018-02-19", until="2018-04-17")]

        f = open('tweets_bajaj.txt', 'w')
        for tweet in tweets:
            print_info(tweet)
            f.write(json.dumps(tweet['created_at'] + tweet['user']['screen_name'] + ' !!!! ' + tweet['text']) + '\n')

def query_tata():
    query = 'TATACHEM OR TATACOMM OR TATAELXSI OR TATAGLOBAL OR TATAMOTORS OR TATAMTRDVR OR TATAPOWER OR TATASTEEL OR TCS OR TATACOFFEE OR TATAINVEST OR TATAMETALI OR TATASPONGE OR TTML'

    for it in range(1):
        tweets = [json.loads(str(raw_tweet)) for raw_tweet
                  in myApi.GetSearch(term=query, count=200, since="2018-03-19", until="2018-04-17")]

        f = open('tweets_tata.txt', 'w')
        for tweet in tweets:
            print_info(tweet)
            f.write(json.dumps(tweet['created_at'] + tweet['user']['screen_name'] + ' %%%% ' + tweet['text']) + '\n')

#
def query_hero():
    query = 'HEROMOTOCO OR "Hero Motocorp" OR HEROHONDA OR "Brijmohan Lall Munjal" OR "Pawan Munjal" OR "Hero Cycles"'

    for it in range(1):
        tweets = [json.loads(str(raw_tweet)) for raw_tweet
                  in myApi.GetSearch(term=query, count=200, since="2018-03-19", until="2018-04-17")]

        f = open('tweets_hero.txt', 'w')
        for tweet in tweets:
            print_info(tweet)
            f.write(json.dumps(tweet['created_at'] + tweet['user']['screen_name'] + ' %%%% ' + tweet['text']) + '\n')

def main():
    print "\n\n\n************ query() ****************\n"
query_reliance()
query_bajaj()
query_tata()
query_hero()
pass


if __name__ == '__main__':
    main()