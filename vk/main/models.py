from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile_picture = models.ImageField(upload_to='templates/media')

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    publication_date = models.CharField(max_length=100)
    #likes

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    #likes

class Friend(models.Model):
    from_user = models.ForeignKey(UserProfile, related_name='friends_from',on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserProfile, related_name='friends_to',on_delete=models.CASCADE)

    class Meta:
        unique_together = ('from_user', 'to_user')  # Prevent duplicate friend requests