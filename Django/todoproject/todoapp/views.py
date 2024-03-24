from django.shortcuts import render
from .models import Todos
from django.http import HttpResponse
# Create your views here.

def index(request):
    
    # create Todos
    # Todos.objects.create(
    #     title="hello 2",
    #     description="hello description",
    #     status="pending"
    # )

    count =  Todos.objects.count()
    print(count)
    # for todo in queryset:
    #     print(todo.title)
    #     print(todo.status)

    return HttpResponse('heloo')
