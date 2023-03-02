from django.db import models
from user . models import User

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=255,blank=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='send')
    reciever = models.ForeignKey(User,on_delete=models.CASCADE,related_name='recieve')
    
class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom,on_delete=models.CASCADE,default = False)
    sender = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)