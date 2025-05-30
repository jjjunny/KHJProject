from django.db import models
from accounts.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    participants = models.ManyToManyField(User, related_name='chatrooms')

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
