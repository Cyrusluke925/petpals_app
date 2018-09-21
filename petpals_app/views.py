from django.shortcuts import render, redirect
from petpals_app.forms import UserForm, UserProfileInfoForm, PostForm, LikeForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import User, UserProfileInfo, Post, Like

#for image upload
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.core import serializers
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(request, 'petpals_app/index.html')

def sendJsonUsers(request):
    users = list(User.objects.all().values('username', 'email'))
    return JsonResponse({'users': users})


def sendJsonPosts(request):
    posts = list(Post.objects.all().values('image', 'caption', 'created_at', 'user'))
    return JsonResponse({'posts': posts})

def sendJsonLikes(request):
    likes = list(Like.objects.all().values('post', 'user'))
    return JsonResponse({'likes': likes})
    

@login_required
def special(request):
    return HttpResponse('You are already logged in.')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form= UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

            login(request, user)
            return redirect('profile_create')
        else: 
            print(user_form.errors)
    else: 
        user_form = UserForm()
    return render(request, 'petpals_app/registration.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                #need to change the path for this redirect to base/feed when we create the template
                return redirect('feed')
            else: 
                return HttpResponse('Your account is inactive.')
        else:
            print('Login Failed')
            print(f'they used username: {username} and password: {password}')
            return HttpResponse('Invalid login details given')
    else:
        #We might need to change the path when we create this form
        return render(request, 'petpals_app/login.html', {})



#LOGIN REQUIRED IF TIME
def profile_create(request):
    print(request.user)
    print('entered profile create')
    #add registered false and true
    if request.method == "POST":
        print('method is a post ')
        
        profile_form = UserProfileInfoForm(request.POST, request.FILES)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            #make a redirect to profile_view
            return render(request, 'petpals_app/profile_view.html')
        else: 
            print(profile_form.errors)
    else:
        form = UserProfileInfoForm()
    print('about to render')
    return render(request, 'petpals_app/profile_create.html', {'form': form})



@login_required
# @csrf_exempt
def feed(request):
    posts = Post.objects.order_by('-created_at')
    form = LikeForm()
    return render(request, 'petpals_app/feed.html', {'form':form, 'posts': posts})


    posts = Post.objects.order_by('-created_at')
    return render(request,'petpals_app/feed.html', {'posts':posts})

def profile_view(request):
    user = request.user
    print(f'the user is {request.user}')
   
    return render(request, 'petpals_app/profile_view.html', {'user': user})


@csrf_exempt
def post_like(request, pk):

    if Like.objects.filter(post=pk, user=request.user.id).exists():
        print('THIS EXISTS')
    else:
        if request.method == "POST":
            print("USER: ")
            print(request.user.id)

            like = Like(post_id=pk, user=request.user)
            like.save()
        # hell yeah!
            return JsonResponse({'message': f'{request.user.username} liked the post with id of {pk}'})



@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            caption = form.cleaned_data.get('caption')
            created_at = timezone.datetime.now()
            if 'image' in request.FILES:
                image = form.cleaned_data.get('image')
                image=request.FILES['image']
            post = Post(caption=caption, image=image, created_at=created_at,user=request.user)
            print(post)
            post.save()
            return redirect('feed')
        else: 
            print('form invalid')
            # return render(request,'petpals_app/post.html'),{'Error': 'There was an error with your post. Please re-upload image.'}
    else: 
        form = PostForm()
        return render(request,'petpals_app/post.html', {'form':form})

