from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
from twitter_app.forms import AddTweetForm
# Create your views here.

def index(request):
    all_tweets = models.Tweet.objects.all()
    tweets_dict = {"tweets" : all_tweets} 
    return render(request,'twitter_app/index.html', context=tweets_dict)

def addtweet(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        models.Tweet.objects.create(nickname=nickname, message=message)
        return redirect(reverse('twitter_app:index'))
    else:
        return render(request,'twitter_app/addtweet.html')
    
def addtweetbyform(request):
    if request.POST:
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname = nickname, message=message)
            return redirect(reverse('twitter_app:index'))
        else:
            print("Error")
            return render(request,'twitter_app/addtweetbyform.html',context={"form":form})
    else:  
        form = AddTweetForm()
        return render(request,'twitter_app/addtweetbyform.html',context={"form":form})
