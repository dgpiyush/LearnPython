from django.urls import path

from . import views

urlpatterns = [
    path('posts/list/', views.index, name='index'),
    path('posts/<id>', views.post_detail, name='post_detail'),
    path('posts/<id>/delete', views.delete_post, name='delete_post'),

    path('posts/add/', views.post_add),
    path('about/', views.about),
    path('teams/', views.teams),
    path('teams/<id>', views.team_detail),
]