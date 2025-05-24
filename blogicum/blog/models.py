from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        'Location',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.SET_NULL
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Location(models.Model):
    name = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
