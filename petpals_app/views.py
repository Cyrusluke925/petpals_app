from django.shortcuts import render, redirect
from petpals_app.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User, UserProfileInfo

#for image upload
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'petpals_app/index.html')

#test page
def test(request):
    return render(request, 'petpals_app/test.html')

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
                return redirect('petpals_app/test.html')
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
    if request.method == "POST" and request.FILES['profile_picture']:
        print('method is a post ')
        
        profile_form = UserProfileInfoForm(data=request.POST)

        if profile_form.is_valid():
            profile_picture = request.FILES['profile_picture']
            fs = FileSystemStorage()
            filename = fs.save(profile_picture.name, profile_picture)
            uploaded_file_url = fs.url(filename)
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            #make a redirect to profile_view
            return render(request, 'petpals_app/test.html', {'uploaded_file_url': uploaded_file_url})
        else: 
            print(profile_form.errors)
    else:
        form = UserProfileInfoForm()
    print('about to render')
    return render(request, 'petpals_app/profile_create.html', {'form': form})



