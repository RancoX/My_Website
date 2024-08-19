from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author} at {self.date_posted}"

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
    

class BucketList(models.Model):
    name=models.CharField(max_length=200)
    link=models.URLField(max_length=300)
    date_added=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"BucketList: {self.name}"
