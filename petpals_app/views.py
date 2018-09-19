from django.shortcuts import render, redirect
from petpals_app.forms import UserForm, UserProfileInfoForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import User, UserProfileInfo, Post


def index(request):
    return render(request, 'petpals_app/index.html')

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
                return redirect('index')
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
        profile_form = UserProfileInfoForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            #make a redirect to profile_view
            return redirect('index')
        else: 
            print(profile_form.errors)
    else:
        form = UserProfileInfoForm()
    print('about to render')
    return render(request, 'petpals_app/profile_create.html', {'form': form})

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
            return render(request,'petpals_app/post.html', {'form':form})
        else: 
            return render(request,'petpals_app/post.html'),{'Error': 'There was an error with your post. Please re-upload image.'}
    else: 
        form = PostForm()
        return render(request,'petpals_app/post.html', {'form':form})

