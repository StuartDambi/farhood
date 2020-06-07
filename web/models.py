from django.db import models
from django.contrib.auth.models import User


class PostCategory(models.Model):
    name = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    # todo: Enable a user to have many Posts --Post.objects.filter(author=user)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=300)
    photo = models.ImageField()
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def postimageurl(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
