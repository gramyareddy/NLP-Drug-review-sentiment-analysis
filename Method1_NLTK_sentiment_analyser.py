from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import pandas as pd
nltk.download('vader_lexicon') 
"""
NLTK already has a built-in, 
pretrained sentiment analyzer called VADER (Valence Aware Dictionary and sEntiment Reasoner).
"""
sia = SentimentIntensityAnalyzer()
df = pd.read_csv("drugsComTrain_raw.csv")


def get_sentiment_score(text):
    scores = sia.polarity_scores(text)
    return scores

def get_sentiment_from_scores(scores):
    pos = scores['pos']
    neu = scores['neu']
    neg = scores['neg']
    if((pos > neg) and (pos > neu) and (pos> 0.7 )):
        return "POS"
    elif((neg > pos) and (neg > neu) and (neg > 0.6)):
        return "NEG"
    else:
        return "NEU"

def get_sentiment_from_rating(rating):
    if(rating > 6):
        return "POS"
    elif(rating < 5):
        return "NEG"
    else:
        return "NEU"
df_results_accurate = pd.DataFrame()
df_results_inaccurate = pd.DataFrame()
total_correct = 0

def store_results(text,rating,sentiment_review,sentiment_rating):
    global df_results_accurate ,df_results_inaccurate
    ds = pd.Series(data= [text,rating,sentiment_review])
    if(sentiment_rating == sentiment_review):
        df_results_accurate = df_results_accurate.append(ds,ignore_index=True)
    else:
        df_results_inaccurate = df_results_inaccurate.append(ds,ignore_index=True)



for i in range(len(df)):
    text = df['review'][i]
    scores = get_sentiment_score(text)
    sentiment_review = get_sentiment_from_scores(scores)
    rating = df['rating'][i]
    sentiment_rating = get_sentiment_from_rating(rating)
    if(sentiment_rating == sentiment_review):
        total_correct += 1
    print("Live Results: ",i, total_correct , len(df))
    if(sentiment_rating != "NEU"):
        store_results(text,rating,sentiment_review,sentiment_rating)

print("Sentiment analysis score = ",int((total_correct*100)/len(df)),total_correct,len(df))
df_results_accurate.to_csv("Correct_sentiment_analysis.csv")
df_results_inaccurate.to_csv("Incorrect_sentiment_analysis.csv")