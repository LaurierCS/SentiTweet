#NOTE: Install dependencies using pip install -r /path/to/requirements.txt command
import tweepy as twp
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class tweet:
    def __init__(self,bearer_token,consumer_key,consumer_secret,access_token,access_token_secret,id):
        # Create a client that is used throughout the object data structure
        self.client = twp.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret,return_type=dict)

        # URL
        self.url = id
        #TODO: add condition to set ID case based (mobile app or normal URL) - Try this on the API call and if this doesnt work try the alternative
        # Another way would be to check if the length and type (all digits) match
        self.id = id #url.split("/")[-1]

        #NOTE:UNIQUE VALUES - set by utilizing inner methods
        #Twitter API V2 Returns
        self.retweets,self.quoteTweets,self.likes,self.replies,self.text=None,None,None,None,None #Creates fields to set to 
        
        # Sentiment Analysis - set from set_data()>sentiment()
        self.polarity = None 
        self.negative = None
        self.positive = None
        self.neutral = None

        # Common Inner Method - Sets Data to the fields declared above
        self.set_data() # sets their data
        return

    def set_data(self): #NOTE: Inner method (Twitter API V2)
        data = self.client.get_tweet(self.id,tweet_fields="public_metrics")['data']
        data_publicMetrics = data['public_metrics']
        # Type cast to make conditional organizing and filtering easier
        self.retweets = int(data_publicMetrics['retweet_count'])
        self.quoteTweets = int(data_publicMetrics['quote_count'])
        self.likes = int(data_publicMetrics['like_count'])
        self.replies = int(data_publicMetrics['reply_count'])
        self.text = data['text']
        self.sentiment()
        return

    def sentiment(self): #NOTE: Inner method (Textblob Sentiment Analysis)
        # calls the data method
        sent_obj = SentimentIntensityAnalyzer()
        sent_dict = sent_obj.polarity_scores(self.text)
        self.polarity,self.negative,self.positive,self.neutral = sent_dict['compound'],sent_dict['neg'],sent_dict['pos'],sent_dict['neu']
        return

    def get_data(self): #NOTE: Method for External Access To Data
        return self.retweets,self.quoteTweets,self.likes,self.replies,self.text,self.polarity,self.negative,self.positive,self.neutral

    def __str__(self): #NOTE: print(classObject)
        return "Tweet: {}\n\nPublic Metrics:\n   Likes: {}\n   Replies: {}\n   Retweets: {}\n   Quote Tweets: {}\n\nSentiment:\n  Polarity: {}\n  Conclusion: {}".format(self.text,self.likes,self.replies,self.retweets,self.quoteTweets,self.polarity,"Some words to describe the sentiment determined through the polarity")
