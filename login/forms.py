from django import forms
from django.contrib.auth.models import User
from .models import userInfo

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
         model = User
         fields = ('username','password','email')

class userInfoForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields =['facebook_id','profile_pic']
