from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('teams/', views.teams),
    path('teams/<id>', views.team_detail),
]