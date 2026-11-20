from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),

    re_path(r'^management(?:/.*)?$', views.management),

    re_path(r'^about(?:/.*)?$', views.about),

    path('contacts/', views.contacts),
    path('news/', views.news),
    path('contacts/<str:country>/', views.contacts_country),
    path('news/<str:othernews>/', views.other_news),
]