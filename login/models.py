from django.db import models
from django.contrib.auth.models import User

# By the Builtin User Model we get username,pass,email

# Create your models here

class userInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    facebook_id = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'media/profile_pics', blank=True)

    def __str__(self):
        return self.user.username
