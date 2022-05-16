from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('register/register',views.register,name='register'),
    path('login/',views.Login,name='login'),
    path('login/login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('count',views.count,name='count')
]