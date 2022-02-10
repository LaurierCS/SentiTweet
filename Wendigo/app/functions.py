from nltk import tokenize, FreqDist
from pytrends.request import TrendReq

def wordCloud(sent): #NOTE: Takes a sentence and returns the most frequent words for the word cloud
    words = tokenize.word_tokenize(sent) #tokenize the sentence
    freq = [s[0] for s in FreqDist(words).most_common() if s[0].isalpha()] # sort by occurance and filter by alphabets
    return freq # return type is list

def getTrendList():
    # returns a 2D list where item 0 is a string of the trending topic and item at index 1 is the link to be used as an HREF
    return [[val,"https://twitter.com/hashtag/{}".format(val.replace(" ",""))] for val in TrendReq().trending_searches(pn='united_states')[0]] # get the top 20 google trends