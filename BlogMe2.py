# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 21:47:26 2023

@author: EZRA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


data = pd.read_excel('C:/Users/EZRA/Downloads/Python and Tableau Course/articles.xlsx')

data.head()
data.info()



keyword = 'crash'

leng= len(data)
marked = []


for x in range(0,leng):
    title = data['title'][x]
    try:
        if keyword in title:
            mark = 1
        else:
            mark = 0
    except:
        mark = 0
    marked.append(mark)
     
#=============================================================================
    
#creating a fuction

    
leng= len(data)

marked = []

def keyflag(keyword):

    for x in range(0,leng):
        title = data['title'][x]
        try:
            if keyword in title:
                mark = 1
            else:
                mark = 0
        except:
            mark = 0
        marked.append(mark)
    return marked
    
bg=keyflag('murder')

mm=pd.Series(bg)



data['keyflag']= mm




data['keyflag'].value_counts()

bbc= data.loc[(data['keyflag']== 1)]


#=============================================================================


#SentimentIntensityAnalyzer

initial_sent = SentimentIntensityAnalyzer()

title= data['title'][1]

senti=initial_sent.polarity_scores(title)


neg= senti['neg']
pos = senti['pos']
neu = senti['neu']

#=============================================================================

#adding for loop to extract sentiments from the titile column

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

lenght = len(data)

for x in range (0,lenght):
    try:
        title= data['title'][x]
        initial_sent = SentimentIntensityAnalyzer()
        senti=initial_sent.polarity_scores(title)
        neg= senti['neg']
        pos = senti['pos']
        neu = senti['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
#==============================================================================
    
#converting list into series

title_neg_sentiment= pd.Series(title_neg_sentiment)
title_pos_sentiment= pd.Series(title_pos_sentiment)
title_neu_sentiment= pd.Series(title_neu_sentiment)


#Creating new columns using the new series converted

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

#=============================================================================

#creating an excel file using the data table

data.to_excel('BlogMe2Clean.xlsx',sheet_name = 'BlogMeData',index = False)














































































































