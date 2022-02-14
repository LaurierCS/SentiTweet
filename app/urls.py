from django.urls import path 
from . import views # import views from the current directory we are in

urlpatterns = [
    path("", views.homepage_view, name="homepage"), # Homepage view
    path("result/<str:tweet_id>",views.results_view,name="result"), # Result page view
]