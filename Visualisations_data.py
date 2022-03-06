import pandas as pd
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns

## read csv(train)
df = pd.read_csv("drugsComTrain_raw.csv")
print(df.head())

## Finding the best rated drugs
sns.set(font_scale = 1.5)
plt.rcParams['figure.figsize'] = [15, 8]

rating = dict(df.loc[df.rating == 10, "drugName"].value_counts())
drugname = list(rating.keys())
drug_rating = list(rating.values())

sns_rating = sns.barplot(x = drugname[0:20], y = drug_rating[0:20])

sns_rating.set_title('Top 20 drugs with 10/10 rating')
sns_rating.set_ylabel("Number of Ratings")
sns_rating.set_xlabel("Drug Names")
plt.setp(sns_rating.get_xticklabels(), rotation=90)
plt.savefig('best_rated.jpg')


## Finding the worst rated drugs



rating = dict(df.loc[df.rating == 1, "drugName"].value_counts())
drugname = list(rating.keys())
drug_rating = list(rating.values())

sns_rating = sns.barplot(x = drugname[0:20], y = drug_rating[0:20])

sns_rating.set_title('Top 20 drugs with 10/10 rating')
sns_rating.set_ylabel("Number of Ratings")
sns_rating.set_xlabel("Drug Names")
plt.setp(sns_rating.get_xticklabels(), rotation=90)
plt.savefig('worst_rated.jpg')



##########3 Positive rated(>7) ############


rating = dict(df.loc[df.rating > 7, "drugName"].value_counts())
drugname = list(rating.keys())
drug_rating = list(rating.values())
print(len(drugname))
with open("Positive_rated_drugs.txt","w") as file:
    file.write('\n'.join(drugname))
sns_rating = sns.barplot(x = drugname[:50], y = drug_rating[:50])

sns_rating.set_title('Positive_rated')
sns_rating.set_ylabel("Number of Ratings")
sns_rating.set_xlabel("Drug Names")
plt.setp(sns_rating.get_xticklabels(), rotation=90)
plt.savefig('Positive_rated.jpg')


## Finding Negatively rated

rating = dict(df.loc[df.rating < 5, "drugName"].value_counts())
drugname = list(rating.keys())
drug_rating = list(rating.values())
print(len(drugname))
with open("Negative_rated_drugs.txt","w") as file:
    file.write('\n'.join(drugname))
sns_rating = sns.barplot(x = drugname[:50], y = drug_rating[:50])

sns_rating.set_title('Negative_rated')
sns_rating.set_ylabel("Number of Ratings")
sns_rating.set_xlabel("Drug Names")
plt.setp(sns_rating.get_xticklabels(), rotation=90)
plt.savefig('Negative_rated.jpg')



## SO a user can be cautious from using the drug if its rated so bad..... and maybe cant used the best rated drug blindly
## but can be a little less cautious using it(after a consultation) 
