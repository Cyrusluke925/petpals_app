from django.shortcuts import render, redirect
from petpals_app.forms import UserForm, UserProfileInfoForm, PostForm, LikeForm, CommentForm, FollowForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import User, UserProfileInfo, Post, Like, Comment, Follow
from django.db.models import Q

#for pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

#for image upload
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.core import serializers
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt


def other_profile(request, pk):
    user = User.objects.get(id=pk)
    posts = Post.objects.filter(user=pk)
    return render(request, 'petpals_app/other_profile.html', {'user': user, 'posts': posts})

def index(request):
    return render(request, 'petpals_app/index.html')


def about(request):
    return render(request, 'petpals_app/about.html')

def user_feed(request):
    print(request.user.id)
    posts = list(Post.objects.filter(
            Q(user=request.user.id) | Q(user__user_to__user_from=User.objects.get(pk=request.user.id))
        ).values('post','user')
        )
    return JsonResponse({'posts': posts})

def sendJsonUsers(request):
    users = list(User.objects.all().values('username', 'email'))
    return JsonResponse({'users': users})


def sendJsonPosts(request):
    posts = list(Post.objects.all().values('image', 'caption', 'created_at', 'user'))
    return JsonResponse({'posts': posts})

def sendJsonLikes(request):
    likes = list(Like.objects.all().values('post', 'user'))
    return JsonResponse({'likes': likes})
    
def sendJsonFollows(request):
    follows = list(Follow.objects.all().values('user_to', 'user_from'))
    return JsonResponse({'follows': follows})

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
        
        form = UserProfileInfoForm(request.POST, request.FILES)
        from django.conf import settings
        print('settings media root {}'.format(settings.PICTURE_ROOT))
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            #make a redirect to 
            
            print(request.POST)
            print(request.FILES)

            return render(request, 'petpals_app/profile_view.html')
        else: 
            print(form.errors)
            return render(request, 'petpals_app/profile_create.html', {'form': form})

    print('about to render')
    form = UserProfileInfoForm()

    return render(request, 'petpals_app/profile_create.html', {'form': form})




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
        # print('logged in:', request.user)
        posts = Post.objects.filter(
            Q(user=request.user.id) | Q(user__user_to__user_from=User.objects.get(pk=request.user.id))
        ).distinct().order_by('-created_at')
        form = CommentForm()
        
        for post in posts:
            likes = Like.objects.filter(post=post)
            print(list(likes))
            print('END')
            
            likes = likes.all().count()
            print(likes)
            post.likes = likes


        return render(request,'petpals_app/feed.html',{'posts':posts, 'form':form})

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

@csrf_exempt
def follow(request, pk):
    user_to = User.objects.get(id=pk)
    if Follow.objects.filter(user_to=pk, user_from=request.user.id).exists():
        print('THIS EXISTS')
        print('here')
    else:
        if request.method == "POST":
            print("USER: ")
            print(request.user.id)
            print ('USER TO:')
            print (user_to.id)
            follow = Follow(user_to=user_to, user_from=request.user)
            follow.save()  
            return JsonResponse({'message': f'{request.user.username} followed the user with id of {pk}'})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(request.FILES)
        print(form.errors)
        print('first')

        # TODO: This code replaces django's form validation because it
        # was missing our image - replace this code with proper validation
        try:
            caption = request.POST['caption']
            image = request.FILES['image']
        except KeyError as e:
            return HttpResponse('Form invalid, missing key {}'.format(e))


        created_at = timezone.datetime.now()
        image = request.FILES['image']
            
        post = Post(caption=caption, image=image, created_at=created_at, user=request.user)
        print(post)
        post.save()
        return redirect('feed')
    else: 
        form = PostForm()
        return render(request,'petpals_app/post.html', {'form':form})

def profile_view(request):
    user = request.user
    posts = Post.objects.filter(user = request.user)
    return render(request, 'petpals_app/profile_view.html', {'user': user ,'posts': posts})

@login_required
def explore(request):
    photos = Post.objects.exclude(
            Q(user=request.user.id) | Q(user__user_to__user_from=User.objects.get(pk=request.user.id))
            ).order_by('?')
    # photos = Post.objects.exclude(user=request.user.id).order_by('?')
    # Increase number of posts when database is full
    print(photos)
    paginator = Paginator(photos, 9)
    page = request.GET.get('page')
    photos = paginator.get_page(page)
    
    return render(request,'petpals_app/explore.html', {'photos':photos})

@login_required
def profile_edit(request):
    user = User.objects.get(id=request.user.id)
    print(user.profile.name)
    # Created not referenced elsewhere because function requires a tuple
    user, created  = UserProfileInfo.objects.get_or_create(user=user)
    user.save()
    if request.method == "POST":
        form = UserProfileInfoForm(request.POST, instance=user)
        print('in PUT')
        if form.is_valid():
            print('form is valid')
            user = form.save()
            if 'profile_picture' in request.FILES:
                print('pic in req')
                user.profile_picture = request.FILES['profile_picture']
            user.save()
            return redirect('profile_view')
    else:
        print('method was {}'.format(request.method))
        form = UserProfileInfoForm(instance=user)
    return render(request, 'petpals_app/profile_edit.html', {'form': form, 'user': user})
    

def view_likes(request):


    the_likes = list(Like.objects.all())
    like_list = []
    for like in the_likes:
        if like.post.user == request.user:
            like_list.append(like)
            print(like_list)
    return render(request, 'petpals_app/view_likes.html', {'like_list': like_list})