from django import forms
from django.contrib.auth.models import User
from petpals_app.models import UserProfileInfo, Post, Like, Comment, Follow


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match, please try again!")


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('name', 'breed', 'age', 'profile_picture', 'bio')

class PostForm(forms.ModelForm):
    class Meta():
        model = Post 
        fields = ('image','caption')

class ProfileEditForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('name', 'breed', 'age', 'profile_picture', 'bio')
        
    # def clean(self):
    #     cleaned_data = super(UserProfileInfoForm, self).clean()
    #     age = cleaned_data.get("age")

    #     if not isinstance(age,int):
    #         raise forms.ValidationError("Please enter a number for pet's age.")

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
