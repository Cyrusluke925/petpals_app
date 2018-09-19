from django.urls import path
from petpals_app import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('login', views.user_login, name='user_login'),
    path('profilecreate', views.profile_create, name='profile_create'),
]
