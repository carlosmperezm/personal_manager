from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

def todo_index(request):
    todos = Todo.objects.filter(title__contains = request.GET.get('search','').strip())
    context = { 'todos': todos }

    return render(request, 'todo/index.html', context)


def create_todo(request):

    if request.method == 'GET':
        form = TodoForm()
        context = { 'form': form }

        return render(request, 'todo/todo_form.html', context)

    elif request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('todo_index')


def update_todo(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == 'GET':
        form = TodoForm(instance=todo)
        context = { 'form': form, 'id':id}

        return render(request, 'todo/todo_form.html',context)

    elif request.method == 'POST':
        updated_todo = TodoForm(request.POST, instance=todo)

        if updated_todo.is_valid():
            updated_todo.save()

            context = { 'form': updated_todo, 'id': id}

            message = 'Todo updated successfully'
            messages.success(request, message)


            return render(request, 'todo/todo_form.html', context)


def view_todo(request, id):
    todo = Todo.objects.get(id = id)
    context = { 'todo': todo }
    return render(request, 'todo/todo_view.html', context)



def delete_todo(request, id):
    todo = Todo.objects.filter(id = id).delete()

    return redirect('todo_index')
