# NLP-Drug-review-sentiment-analysis
UCI DRUG REVIEW ANALYSIS
=============================

I have taken the dataset and tried a few basic EDA.

In Visualisations_data.py
===========================
I pick out the top rated and least rated drugs as from a user point of view, these are essential , to know if the drug has a low erating(and hence is not so safe for use) and they can avoid it.
Also created a list of all the drugs rated Positively ( more than 7) and the ones rated negatively (less than 5). Neutral not listed.

In Method1_NLTK_sentiment_analyser.py
=====================================
I tried to use NLTK s inbuilt polarity score generator but the accuracy wasnt good. SO tried to build a model for this dataset.

In Method2_Sentiment_Analysis_DRUG_REVIEW.ipynb
================================================
I clean up the data (removing punct, stopwords(most frequent used ones) , etc) and generate more features based on review length , unique words etc.
make it a binary classification(0or1 , pos or neg review, >5,<=5)
and trained it on a few classifiers(models in models directory ):
Accuracy 
1. XGBClassifier :  88.79%
2. LGBMClassifier : 75.88 %
3. CatBoostClassifier :  88.24%
