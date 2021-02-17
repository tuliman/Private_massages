from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    city = models.CharField(max_length=50,blank=True)

class Chats(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Person_1')
    opponent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Person_2')


class Messages(models.Model):
    chat_id = models.ForeignKey(Chats, on_delete=models.CASCADE, verbose_name='Chat')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Name')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    news =models.ForeignKey(News,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    file = models.FileField(blank=True,upload_to='media/file/')
    image = models.ImageField(blank=True,upload_to='media/comments/images/')
    create = models.DateTimeField(auto_now_add=True)
