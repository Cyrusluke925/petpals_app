from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.utils import timezone

# Create your models here.

# age_form =forms.CharField(min_length=7, validators=[])

# RegEx Validtors
def _get_breed_validator():
    return RegexValidator('^[a-zA-Z ]+$', message="Breeds can only allow uppercase letters, lowercase letters, and spaces")

class UserProfileInfo(models.Model):
    name = models.CharField(max_length=40)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True,  upload_to=settings.MEDIA_ROOT, null=True, default=settings.MEDIA_ROOT+'/pawprint.png')
    breed = models.CharField(max_length=40, blank=True, null=True, validators=[_get_breed_validator()])
    age = models.PositiveIntegerField(blank=True, null=True,  validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#make onetoone later
    def __str__(self):
        return self.user.username

class Post(models.Model):
    caption = models.TextField(blank=True, max_length=255, default="", null=True)
    image = models.ImageField(upload_to=settings.PICTURE_ROOT)
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='post')  

    def created_at_formatted(self):
        return self.created_at.strftime('%b %e %Y')

class Comment(models.Model):
    content = models.CharField(max_length=300, default="")
    # created_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)    
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')

    # def created_at_formatted(self):
    #     return self.created_at.strftime('%b %e %Y')

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")

    def __str__(self):
        return self.user.username

class Follow(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_from')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_to")

    def __str__(self):
        return self.user_from.username
