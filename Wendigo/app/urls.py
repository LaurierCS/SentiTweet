from django.urls import path 
from . import views # import views from the current directory we are in

urlpatterns = [
    # type the id and it will pop up the name of the todo list and the items it contains
    # Homepage
    # Results Page

    path("", views.homepage_view, name="homepage"),
    path("result/<str:tweet_id>",views.results_view,name="result"), # result will call the path after this and populate it with info?
    #path("<str:tweet_id>", views.index, name="index"), # if we get into this app and if we are in the home page, go to the views.index page that has the name index
]