from django.shortcuts import render
from todo_app.models import Todo
from django.http import HttpResponseRedirect

def todo_list(request):
    todos = Todo.objects.all()
    return render(
        request,
        "todo_list.html",
        {"todos":todos },
    )

def todo_create(request):
    if request.method == "GET":
        return render(request,"todo_create.html")
    else:
        title = request.POST["title"]
        Todo.objects.create(title=title)
        return HttpResponseRedirect("/")


def todo_delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect("/")
        
def todo_update(request,id):
    if request.method == "GET":
        todo = Todo.objects.get(id=id)
        return render(
            request,
            "todo_update.html",
            {"todo":todo},
            )
    else:
        todo = Todo.objects.get(id=id)
        todo.title = request.POST["title"]
        todo.save()
        return HttpResponseRedirect("/")


