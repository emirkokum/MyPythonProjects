from django.contrib import admin
from django.urls import path
from . import views

app_name = "twitter_app"

urlpatterns = [
    path('',views.index,name="index"), #123123123123/twitter_app
    path('addtweet/',views.addtweet,name="addtweet"), #123123123123/twitter_app/addtweet
    path('addtweetbyform',views.addtweetbyform,name="addtweetbyform")
]
