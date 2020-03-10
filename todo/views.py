from django.shortcuts import render
from .models import Task
from .forms import TaskFrom
from django.shortcuts import redirect


def index(request):
    if request.method == 'POST':
        task = TaskFrom(request.POST)
        if task.is_valid():
            task = task.save(commit=False)
            task.complete = False
            task.author = request.user
            task.save()
            return redirect('/')
    elif request.user.is_authenticated:
        tasks = Task.objects.filter(author=request.user)
        form = TaskFrom()
        return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})
    else:
        return redirect('/accounts/login')



def update(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task = TaskFrom(request.POST, instance=task)
        if task.is_valid():
            task.save()
            return redirect('/')
    else:
        form = TaskFrom(instance=task)
        return render(request, 'todo/update.html', {'form': form})


def delete(request, pk):
     task = Task.objects.get(id=pk)
     task.delete()
     return redirect('/')

def complete(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = not task.complete
    task.save()
    return redirect('/')
