from email.policy import default
from django.db import models


class Query(models.Model):
    tweet_id = models.CharField(max_length=200, blank=False) # ID of the tweet as a string (length will be smaller)
    date_created = models.DateTimeField(auto_now_add=True) # add the date created to the model
    def __str__(self):
        return self.tweet_id

class Result(models.Model): #TODO: Add one to one relationship with query and generate the data using the function
    query = models.OneToOneField(Query,on_delete=models.CASCADE)
    # Each query has many results (depending on time)
    # Public Metrics
    likes = models.BigIntegerField()
    replies = models.BigIntegerField()
    retweets = models.BigIntegerField()
    quoteTweets = models.BigIntegerField()
    text = models.TextField(max_length=300,default="");
    # Sentiment
    polarity = models.DecimalField(decimal_places=2,max_digits=4)
    #s_negative = models.DecimalField(decimal_places=4,max_digits=4)
    #s_positive = models.DecimalField(decimal_places=4,max_digits=4)
    #s_neutral = models.DecimalField(decimal_places=4,max_digits=4)