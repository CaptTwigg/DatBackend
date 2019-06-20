from django.contrib import admin
from django.urls import path, include

from Michelle import views

urlpatterns = [
    path('', views.index, name="index"),
]
