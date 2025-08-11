from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    nick = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=60)
    bio = models.CharField(max_length=250)
    password = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)