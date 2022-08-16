import locale
from tkinter import S
import tweepy
import configparser
import pandas as pd
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax





config = configparser.ConfigParser()
config.read('config.ini')


api_key = 'xxx'
api_key_secret = 'xxx'

access_token = 'xxx'
access_token_secret = 'xxx'



def pic_tweet(dirty_tweet):
    
    diced_tweet = [ ]
    
    for word in dirty_tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = "http"

        diced_tweet.append(word)
    merged_tweet = " ".join(diced_tweet)
    
    return merged_tweet



def emotionTensorMap(clean_tweet):
    
    roberta = "cardiffnlp/twitter-roberta-base-sentiment"
    model = AutoModelForSequenceClassification.from_pretrained(roberta)
    tokenizer = AutoTokenizer.from_pretrained(roberta)
    result = [0,0]
    labels = ['Negative', 'Neutral', 'Positive']
    
    clean_tweet = tokenizer(clean_tweet, return_tensors ='pt')
    
    output = model(clean_tweet['input_ids'],clean_tweet['attention_mask'])
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    
    for i in range(len(scores)):
          
        
        if scores[i] >= result[1]:
         result[0] = labels[i]
         result[1] = scores[i]
    
    return result

    
    




auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)




keywords = '#Dota2' + "-filter:retweets"

limit = 1000
tweets = tweepy.Cursor(api.search_tweets,q=keywords, tweet_mode='full_text',locale ='eng').items(1000)
columns = ['Time','User','tweet','Feeling','Tensor Value']
data = []
i = 0
for tweet in tweets:
 i = i +1
 dirty_tweet = tweet.text

 clean_tweet = pic_tweet(dirty_tweet)

 emotion = emotionTensorMap(clean_tweet)

 data.append([tweet.created_at, tweet.user.screen_name, clean_tweet, emotion[0], emotion[1]])
 print('processando...', i)


df = pd.DataFrame(data, columns = columns)
df.to_csv('tweetsEmotion.csv')

dfr = pd.read_csv('tweetsEmotion.csv')

