from django.urls import path
from . import views

urlpatterns = [
    path('detail/<str:title>', views.podcast_detail, name='podcast_detail'),
    path('add/', views.add_podcast, name='add_podcast'),
    path('delete_podcast/<str:title>/', views.delete_podcast, name='delete_podcast'),

]
