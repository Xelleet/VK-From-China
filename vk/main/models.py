from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile_picture = models.ImageField(upload_to='templates/media')

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    publication_date = models.DateField()
    #likes

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    #likes
