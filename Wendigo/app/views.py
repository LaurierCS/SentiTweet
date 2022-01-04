from django.shortcuts import render
from django.http import HttpResponse

# Imports for Django views
from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Import the models 
from .models import Query,Result
from .tweet_class import tweet # to get metrics and polarity


consumer_key = "XZ6WyOzWDLrGTcf9cHqdSv8Lt"
consumer_secret = "7adbmfai6Z3eUwk4uysZiyvFAKg2ZmRcArb93dtBUt7g6aJg1y"
access_token  = "1350238888741236745-KJhi9SEqPnbBSOnEfkqFFa9tlSYQBJ"
access_token_secret = "oKuViYQXdPeIlHWB3s4SZcVoDbuOJY4MH58Pp3gMpgQ00"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAJPoWQEAAAAAYMIXCZFC5gknuHSd6Aded3VUSxE%3D8s9Sn2yAnGCN1CdGHT1MYYu2mlQ6S9xKZNLQuajtoelj2cfDhP"


def homepage_view(request):
    page_title = "Homepage"

    context = {'page_title': page_title}
    template_name = '../templates/base.html'
    return render(request, template_name, context)


def index(response, tweet_id):  
    # TODO: Use the error handling
    ob = Query.objects.create(tweet_id=tweet_id) # take a query URL and add the query to the table (fill the field)
    object = tweet(bearer_token,consumer_key,consumer_secret,access_token,access_token_secret,tweet_id)
    retweets,quoteTweets,likes,replies,text,polarity,__,__,__ = object.get_data()
    rs = Result.objects.create(query=ob,likes=likes,replies=replies,retweets=retweets,quoteTweets=quoteTweets,polarity=polarity) # fill the other fields (null=false?)
    # call the function to get the details (metrics and sentiment)
    response_html = "<h1>{}</h1><br></br><h2>Tweet: {}</h2><br></br><h2>Likes: {}</h2><br></br><h2>Replies: {}</h2><br></br><h2>Polarity: {}</h2><br></br><h2>Retweets: {}</h2><br></br><h2>Quote Tweets: {}</h2>".format(tweet_id,text,likes,replies,polarity,retweets,quoteTweets)
    # add the result to the table and assign the query parent (one to one)
    return HttpResponse(response_html) # create a string with the html code and then pass it here

