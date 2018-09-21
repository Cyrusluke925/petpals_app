from django import forms
from django.contrib.auth.models import User
from petpals_app.models import UserProfileInfo, Post, Like, Comment, Follow


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('name', 'bio', 'profile_picture', 'breed', 'age')

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post 
        fields = ('image','caption')


class LikeForm(forms.ModelForm):

    class Meta():
        model = Like
        fields = ('user', 'post')

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('content',)


class FollowForm(forms.ModelForm):

    class Meta():
        model = Follow
        fields = ('user_to', 'user_from')
