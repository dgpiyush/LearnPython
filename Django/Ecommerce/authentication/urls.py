

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('test/',views.test, name='test'),
    path('activate/<username>/<token>', views.activate, name='activate'),
    path('reset/<username>/<token>', views.reset_view, name='reset'),
    path('forgot-password/', views.forgot_view, name='forgot'),
    path('change-password/', views.change_password, name='change_password'),

]