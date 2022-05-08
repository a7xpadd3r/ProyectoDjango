from distutils.command.upload import upload
from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver

class webUser(models.Model):
    USERNAME_FIELD = models.CharField(max_length=15)
    email = models.EmailField()
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    info = models.TextField(max_length = 500, blank = True)
    avatar = models.ImageField(upload_to = 'avatars', blank = True, null = True)
    
@receiver(post_save, sender = User)
def CreateUserProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        
@receiver(post_save, sender = User)
def SaveUserProfile(sender, instance, **kwargs):
    instance.profile.save()