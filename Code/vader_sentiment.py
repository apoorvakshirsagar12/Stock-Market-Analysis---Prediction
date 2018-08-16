import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk import tokenize
import time
#start=time.time()


# read file
filenames=['tweets_Reliance.csv']
df = pd.read_csv(filenames[0])

def sentiment_cal(tweet):
    sia = SentimentIntensityAnalyzer()
    score= sia.polarity_scores(tweet)
    score = float(score['compound'])
    return score

result = pd.DataFrame()
for i,r in df.iterrows():
    score = sentiment_cal(str(r.tweet))
    temp = pd.DataFrame(
        {'time': [r.time], 'username': [r.username], 'tweet': [r.tweet], 'company': [r.company], 'sentiment': [score],
         'date': [r.date]})
    result = pd.concat([result, temp])
	#print(temp)
#print(result.head(2))

result.to_csv('Labeled_Reliance.csv',encoding='utf-8',sep=',')
#print(time.time()-start)