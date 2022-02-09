from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

STATUS = ((0,'Draft'),(1,'Published'))

class Post(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(default=datetime.now)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)


# Create your models here.
