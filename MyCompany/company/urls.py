from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),

    re_path(r'^news(?:/.*)?$', views.news),

    re_path(r'^management(?:/.*)?$', views.management),

    re_path(r'^about(?:/.*)?$', views.about),

    path('contacts/', views.contacts),
    path('contacts/<str:country>/', views.contacts_country),
]