from django.urls import path
from . import views

app_name= "profile"

urlpatterns = [
    path('signin/', views.user_login, name='login'),
    path('signup/', views.user_register, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]