from django.shortcuts import render, HttpResponse, redirect
from .models import CustomUser as User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.urls import reverse




def index(request):
   
    return  render(request,'index.html')



def login_view(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        callback_url = request.GET.get('next')

        user = authenticate(username=username, password=password)  # verify credentials and return user if valid or else return None

        if user is not None:
            login(request,user)


            if(callback_url): 
                return redirect(callback_url)
            
            return redirect('home')
        else:
            return  render(request,'login.html',{'error':'Invalid credentials'})

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
            my_user = User.objects.create_user(username,email,password, is_active=False)
            my_user.first_name = first_name
            my_user.last_name = last_name
            token = my_user.generate_token()
            my_user.token = token
            my_user.save()

      
            send_mail(
                subject='Activate your account',
                message='',
                from_email="biz.piyushmishra@gmail.com",
                recipient_list=[email],
                fail_silently=False,
                html_message='<a href="http://127.0.0.1:8000/auth/activate/' + my_user.username + '/' + token +  '">Click here to activate your account</a>',
                
            )
            return redirect('login')
    return  render(request,'register.html')


@login_required(login_url='login')
def home(request):
    return  render(request,'home.html')

    

# def home(request):
#     if request.user.is_authenticated:
#         return  render(request,'home.html')
#     else:
#         return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')



def test(request):
    user= "Piyush"
    send_mail(subject="hello", message="", html_message=f"Hello {user}", from_email="biz.piyushmishra@gmail.com", recipient_list=["nagilan902@bsomek.com"])
    return HttpResponse('test')



def activate(request, username,token):
    user = None
    try:
        user = User.objects.get(username=username)
    except:
        pass

    if user is not None:
        if user.token == token:
            user.is_active = True
            user.token = ''
            user.save()
            return redirect('login')
        return HttpResponse('Invalid token')


def forgot_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = get_user_or_none(username)

        if user is not None:
            token = user.generate_token()
            user.token = token
            user.save()

            url = 'http://127.0.0.1:8000' + reverse('reset',kwargs={'username':username,'token':token})

            send_mail(
                subject='Activate your account',
                message='',
                from_email="biz.piyushmishra@gmail.com",
                recipient_list=[user.email],
                fail_silently=False,
                html_message='<a href="' + url + '"">Click here to reset your password</a>',
            )
    

    return render(request,'forgot.html')


def reset_view(request, username,token):
    user = None
    try:
        user = User.objects.get(username=username)
    except:
        pass

    if user is not None:
        if user.token == token:
            if request.method == 'POST':
                password = request.POST.get('password')
                user.set_password(password)
                user.save()
                return redirect('login')
            return render(request,'reset.html')

        return HttpResponse('Invalid token')


def get_user_or_none(username):
    try:
        user = User.objects.get(username=username)
        return user
    except:
        return None