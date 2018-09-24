from django import forms
from django.contrib.auth.models import User
from petpals_app.models import UserProfileInfo, Post, Like, Comment, Follow

class UserForm(forms.ModelForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder':'Username'}
        )
    )

    email = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder':'Email'}
            )
        )
    
    password=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder':'Password'}
            )
        )

    confirm_password=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder':'Confirm Password'}
            )
        )
    class Meta:
        model=User
        fields=('username','email','password')
        help_texts = {
            'username': None,
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match, please try again!")

class UserProfileInfoForm(forms.ModelForm):

    bio=forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'placeholder':'Tell us about your pets'' personality,favorite toys, food, and anything else you''d like to share!'}
            )
        )
    
    class Meta():
        model = UserProfileInfo
        fields = ('name', 'breed', 'age', 'bio','profile_picture')

class PostForm(forms.ModelForm):
    caption=forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'placeholder':'Aww! Enter a caption!'}
            )
        )
    
    
    class Meta():
        model = Post 
        fields = ('image','caption')

class ProfileEditForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('name', 'breed', 'age', 'profile_picture', 'bio')

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
