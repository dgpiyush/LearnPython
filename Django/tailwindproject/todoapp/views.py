from django.shortcuts import redirect, render, HttpResponse

from .models import Todo


def list(request):
    
    queryset =  Todo.objects.all()

    print(queryset.query)

    context = {
        "todos": queryset
    }
    return render(request, 'list-todo.html',context)



def create(request):
    # Todo.objects.create(desc="dummy desc")
    print(request.GET.get('text'))
    print(request.GET.get('csrfmiddlewaretoken'))
 
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        print(title, text, 'title, text')
        Todo.objects.create(title=title, desc=text)
        return redirect('/todoapp')
    

    return render(request, 'create-todo.html')


def update(request, id):
    todo =  Todo.objects.get(id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        status = request.POST.get('status')

        todo.title = title
        todo.desc=  text
        todo.status = status

        todo.save()

        return redirect('/todoapp')
    
    return render(request, 'update-todo.html', {'todo': todo})
  


def delete(request, id):
    # todo =  Todo.objects.get(id=id)
    # todo.delete()
    # return redirect('/todoapp')
    return HttpResponse(id)