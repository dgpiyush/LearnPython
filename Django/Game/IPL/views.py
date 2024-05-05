from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import Team, Player, Post
# Create your views here.


def index(request):
    post_query = Post.objects.all()
    return  render(request, 'index.html', {'posts': post_query })



def post_detail(request, id):

    post = Post.objects.get(id=id)

    return render(request, 'post_detail.html', {'post': post})


def post_add(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        post = Post(title=title, description=description)
        post.save()
        return redirect('/')

    return render(request, 'post_add.html')

def about(request):
    return render(request, 'about.html')



def teams(request):

    queryset =  Team.objects.all()
    print(queryset.query)

    return render(request, 'teams.html', {'teams': queryset})

def team_detail(request,id):

    queryset =  Player.objects.filter(team=id)

    print(queryset)

    return render(request, 'team_detail.html', {'players': queryset})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    # post.delete()
    print(reverse('post_detail',  kwargs={"id": post.id}))

    return redirect(reverse('index'))

