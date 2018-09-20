from django.urls import path
from django.conf.urls import url
from petpals_app import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('login', views.user_login, name='user_login'),
    path('profilecreate', views.profile_create, name='profile_create'),
    path('profile', views.profile_view, name="profile_view"),
    path('post/new', views.post_create, name='post_create'),
    path('feed', views.feed, name='feed'),
    path('explore', views.explore, name='explore'),
]
