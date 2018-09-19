from django.urls import path
from django.conf.urls import url
from petpals_app import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('login', views.user_login, name='user_login'),
    path('profilecreate', views.profile_create, name='profile_create'),
    path('post/new', views.post_create, name='post_create'),
    # url(r'^user/(?P<fk>[0-9]+)', views.post_create, name='post_create'),
]
