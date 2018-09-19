from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.

class UserProfileInfo(models.Model):
    name = models.CharField(max_length=40)
    bio = models.TextField()
    profile_picture = models.ImageField(blank=True, upload_to=settings.MEDIA_ROOT)
    breed = models.CharField(max_length=40, blank=True)
    age = models.IntegerField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#make onetoone later
    def __str__(self):
        return self.user.username

class Post(models.Model):
    caption = models.TextField(blank=True, max_length=255, default="", null=True)
    image = models.ImageField(blank=True, upload_to=settings.PICTURE_ROOT)
    created_at = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='post')    

    def created_at_formatted(self):
        return self.created_at.strftime('%b %e %Y')
