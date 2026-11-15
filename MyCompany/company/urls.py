from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),

    re_path(r'^news(?:/.*)?$', views.news),

    re_path(r'^management(?:/.*)?$', views.management),

    re_path(r'^about(?:/.*)?$', views.about),

    re_path(r'^(?:contacts|contact)(?:/.*)?$', views.contacts),
]