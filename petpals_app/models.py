from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class UserProfileInfo(models.Model):
    name = models.CharField(max_length=40)
    bio = models.TextField()
    profile_picture = models.ImageField(blank=True)
    breed = models.CharField(max_length=40, blank=True)
    age = models.IntegerField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#make onetoone later
    def __str__(self):
        return self.user.username
