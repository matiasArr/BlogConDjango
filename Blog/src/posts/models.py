from turtle import title
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from ckeditor.fields import RichTextField
# Create your models here.

class User(AbstractUser):
    pass

    def get_signup_redirect_url(self, request):
        return reverse("account_login")

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail-post", kwargs={
            'slug': self.slug
        })

    ## NECESITO UNA FUNCION QUE ME RETORNO UN POST EN CONCRETO
    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def serializer(self):
        return {
            'title': self.title,
            'slug': self.slug
        }

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()

    @property
    def get_views_count(self):
        return self.postview_set.all().count()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username