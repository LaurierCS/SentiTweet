# Imports for Django views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Imports for Forms 
from .forms import CreateQuery

# Import the models 
from .models import Query,Result
from .tweet_class import tweet # to get metrics and polarity
# Additional Functions
from .functions import wordCloud

consumer_key = "XZ6WyOzWDLrGTcf9cHqdSv8Lt"
consumer_secret = "7adbmfai6Z3eUwk4uysZiyvFAKg2ZmRcArb93dtBUt7g6aJg1y"
access_token  = "1350238888741236745-KJhi9SEqPnbBSOnEfkqFFa9tlSYQBJ"
access_token_secret = "oKuViYQXdPeIlHWB3s4SZcVoDbuOJY4MH58Pp3gMpgQ00"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAJPoWQEAAAAAYMIXCZFC5gknuHSd6Aded3VUSxE%3D8s9Sn2yAnGCN1CdGHT1MYYu2mlQ6S9xKZNLQuajtoelj2cfDhP"


def homepage_view(response):
    if response.method == "POST":
        form = CreateQuery(response.POST)
        if form.is_valid():
            tweet_url = form.cleaned_data["query"]
            tweet_id = tweet_url.split('/')[-1] #Extract the ID from the URL
            # Check if the tweet_id is valid, if not thorw an error message
            if (len(tweet_id)==19 and tweet_id.isnumeric()): #Conditions for a valid ID
                return HttpResponseRedirect("/result/%s" %tweet_id) # redirect to the right URL and create an entry with the model
            
            # else throw an error message on the HTML page saying its invalid
            return HttpResponseRedirect("/result/%s" %tweet_id) 
    else:
        form = CreateQuery() # Creates a blank form

    page_title = "Homepage"
    context = {'page_title': page_title,"form":form}
    template_name = '../templates/base.html'
    return render(response, template_name, context) # should take in the form for query model as well

def results_view(request,tweet_id):
    page_title = "Result"

    # Generate Twitter API results, Polarity Score and word cloud list everytime the result view is called
    object = tweet(bearer_token,consumer_key,consumer_secret,access_token,access_token_secret,tweet_id) # create tweet class object
    retweets,quoteTweets,likes,replies,text,polarity,neg,pos,neu = object.get_data() # get data from the tweet class object
    wordCloudList = wordCloud(text) # use the text of the tweet to generate a word cloud (freq dist and word filter)

    try: # CASE: If the query model object already exists
        ob = Query.objects.get(tweet_id=tweet_id) # get the object by tweet_id
        rs = Result.objects.get(query=ob) # get the result model object associated with the query object
        # add the new tweet data to the result model object
        rs.likes=likes
        rs.replies=replies
        rs.retweets=retweets
        rs.quoteTweets=quoteTweets
        rs.polarity=polarity 
        rs.text = text
        rs.score_neg = neg
        rs.score_pos = pos
        rs.score_neu = neu

        # save both the models
        rs.save()
        ob.save()
        wordCloudList = wordCloud(text) # use the text of the tweet to generate a word cloud (freq dist and word filter)
    except: # CASE: If the query model object with the same tweet_id does not exist
        ob = Query.objects.create(tweet_id=tweet_id) # take a tweet ID and add it to the query to the table (fill the field)
        rs = Result.objects.create(query=ob,likes=likes,replies=replies,retweets=retweets,quoteTweets=quoteTweets,polarity=polarity,text=text,score_neg=neg,score_pos=pos,score_neu=neu) # fill fields of results object with tweet object data and link it to the query object

    context = {'page_title': page_title,'ob':ob,'rs':rs,'list':wordCloudList}
    template_name = '../templates/results.html'
    return render(request, template_name, context)