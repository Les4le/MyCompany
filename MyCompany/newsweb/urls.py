from django.urls import path
from . import views

app_name = 'newsweb'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('achievements/', views.achievements, name='achievements'),
    path('articles/', views.articles, name='articles'),
    path('announcements/', views.announcements, name='announcements'),
]
