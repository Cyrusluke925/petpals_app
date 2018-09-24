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
    path('user/<int:pk>/profile', views.other_profile, name="other_profile"),
    path('post/new', views.post_create, name='post_create'),
    path('feed', views.feed, name='feed'),
    path('api/users', views.sendJsonUsers, name='sendJsonPosts'),
    path('api/posts', views.sendJsonPosts, name="sendJsonPosts"),
    path('api/likes', views.sendJsonLikes, name="sendJsonLikes"),
    path('post/<int:pk>/like', views.post_like, name="post_like"),
    path('api/feed', views.user_feed, name="user_feed"),
    path('post/<int:pk>/comment',views.comment_create, name="comment_create"),
    path('api/comments', views.sendJsonComments, name="sendJsonComments"),


    path('about', views.about, name='about'),
    
    
    

    path('explore', views.explore, name='explore'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
    path('api/follows', views.sendJsonFollows, name="sendJsonFollows"),
    path('user/<int:pk>/follow', views.follow, name="follow"),
    path('likes', views.view_likes, name='view_likes'),
]
