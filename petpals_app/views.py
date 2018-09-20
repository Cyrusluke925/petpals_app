from django.shortcuts import render, redirect
from petpals_app.forms import UserForm, UserProfileInfoForm, PostForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import User, UserProfileInfo, Post, Comment
#for pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

#for image upload
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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

@login_required
def profile_create(request):
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

def profile_view(request):
    user = request.user
    posts = Post.objects.filter(user = request.user)
    print(posts[1].caption)
    return render(request, 'petpals_app/profile_view.html', {'user': user ,'posts': posts})

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

@login_required
def feed(request): 
    if request.method == 'POST':
        form = CommentForm(request.POST)
        created_at = timezone.datetime.now()
        if form.is_valid():
            content = form.cleaned_data.get('content')
            post_id = request.POST.get('post_id')
            comment = Comment(content=content, created_at=created_at, user=request.user, post_id=post_id)
            print(comment)
            comment.save()
            print('comment post key:', comment.post.pk)
            return redirect('feed')
        else: 
            print('form invalid')
    else: 
        posts = Post.objects.order_by('-created_at')
        form = CommentForm()
        return render(request,'petpals_app/feed.html',{'posts':posts, 'form':form})

@login_required
def explore(request):
    photo = Post.objects.all()
    # Increase number of posts when database is full
    paginator = Paginator(photo, 2)
    page = request.GET.get('page')
    photos = paginator.get_page(page)
    
    return render(request,'petpals_app/explore.html', {'photos':photos})