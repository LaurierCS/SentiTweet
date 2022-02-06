from nltk import tokenize, FreqDist

def wordCloud(sent): #NOTE: Takes a sentence and returns the most frequent words for the word cloud
    words = tokenize.word_tokenize(sent) #tokenize the sentence
    freq = [s[0] for s in FreqDist(words).most_common() if s[0].isalpha()] # sort by occurance and filter by alphabets
    return freq # return type is list