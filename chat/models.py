from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Baned_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Profile')
    is_baned = models.BooleanField(default=False, verbose_name='Baned_user')
    reason = models.CharField(blank=True, max_length=250, verbose_name='related on bans')


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
