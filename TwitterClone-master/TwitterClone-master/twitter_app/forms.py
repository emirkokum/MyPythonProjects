from django import forms
from django.forms import ModelForm
from twitter_app.models import Tweet

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="Nickname",max_length=50) 
    message_input = forms.CharField(label="Message",max_length=150,widget=forms.Textarea(attrs={"class":"tweetarea"}))
