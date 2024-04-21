from django.shortcuts import render, HttpResponse
from .models import Team, Player
# Create your views here.


def index(request):
    names = []
    count_of_name = len(names)
    return  render(request, 'index.html', {'value': "<script> alert('hello') </script>" })


def about(request):
    return render(request, 'about.html')



def teams(request):

    queryset =  Team.objects.all()

    return render(request, 'teams.html', {'teams': queryset})



def team_detail(request,id):

    queryset =  Player.objects.filter(team=id)

    print(queryset)

    return render(request, 'team_detail.html', {'players': queryset})