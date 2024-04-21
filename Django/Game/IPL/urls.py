from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('posts/add/', views.post_add),
    path('about/', views.about),
    path('teams/', views.teams),
    path('teams/<id>', views.team_detail),
]