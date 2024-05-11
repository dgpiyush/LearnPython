from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def index(request):
    return  render(request,'index.html')



def login_view(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

    return  render(request,'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')

        print(username,first_name,last_name,email,phone_number,password,c_password)

        if password == c_password:
            my_user = User.objects.create_user(username,email,password)
            my_user.first_name = first_name
            my_user.last_name = last_name
            my_user.save()
            return redirect('login')
    return  render(request,'register.html')


# @login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        return  render(request,'home.html')
    else:
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')