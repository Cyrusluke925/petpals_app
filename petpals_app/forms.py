from django import forms
from django.contrib.auth.models import User
from petpals_app.models import UserProfileInfo, Post, Like, Comment


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())

#     class Meta():
#         model = User
#         fields = ('username', 'email', 'password')

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
            raise forms.ValidationError(
                "Passwords do not match, please try again!"
            )


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
