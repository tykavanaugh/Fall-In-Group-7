from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    needs = models.CharField(max_length=100)
    urgency = models.CharField(max_length=100)
    details = models.CharField(max_length=1024)

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    vetted = models.BooleanField()
    assistance_type = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
   
class OrgUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

class ChatRoom(models.Model):
    id = models.AutoField(primary_key=True)
    org_user_id = models.ForeignKey(OrgUser,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    password = models.CharField(max_length=100)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=1024)
    org_user_id = models.ForeignKey(OrgUser,on_delete=models.CASCADE)
    chatroom_id = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

class Response(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=1024)
    user_id = models.ForeignKey(OrgUser,on_delete=models.CASCADE)
    message_id = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)




