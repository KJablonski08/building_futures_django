from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
class Comment(models.Model):
    body = models.CharField(max_length=100)
    author = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
