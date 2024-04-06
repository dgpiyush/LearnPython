from django.shortcuts import redirect, render
from .models import Todos
from django.http import HttpResponse, Http404
from django.contrib import messages
# Create your views here.

def index(request, **kwargs):
    queryset = Todos.objects.all()
    return render(request, 'todos.html', {'todos': queryset})

def create(request):
    return render(request, 'create.html')

def save(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        todo = Todos.objects.create(
            title=title,
            description=description,
            status="pending"
        )
        todo.save()
        messages.success(request, 'Todo created successfully')
        return redirect('todos')
    else:
        return HttpResponse('Method not allowed. Use POST') 

def delete(request, id):
    todo = Todos.objects.get(id=id)
    todo.delete()
    messages.success(request, 'Todo deleted successfully')
    return  redirect('todos')

def edit(request, id):
    todo = Todos.objects.get(id=id)
    return render(request, 'edit.html', {'todo': todo})

def update(request, id):
    todo = Todos.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        todo.title = title
        todo.description = description
        todo.status = status
        todo.save()
        messages.success(request, 'Todo updated successfully')
        return redirect('todos')
    else:
        return HttpResponse('Method not allowed. Use POST')

