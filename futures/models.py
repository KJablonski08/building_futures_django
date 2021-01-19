from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        'users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    photo = models.TextField(
        default='http://www.buildingfuturesinc.com/Building_Futures,_Inc./Trip_Photos/Pages/Masai_Mara_files/Media/AEJ_3825/AEJ_3825.jpg?disposition=download')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', default=1)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
