from django.contrib import admin
from django.urls import path
from django_ecology import views

urlpatterns = [
    path('', views.home),
    path('submit_proposal/', views.submit_proposal, name='submit_proposal')
]