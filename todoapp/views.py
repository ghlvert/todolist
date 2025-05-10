from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from todoapp.forms import TaskForm
from todoapp.models import Task

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        tasks = None
    else:
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'todoapp/index.html', {'tasks': tasks})


def detail_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoapp/detail.html', {'task':task, 'form': form})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            url = reverse_lazy('todoapp:detail_task', args=[new_task.id,])
            return redirect(url)
    else:
        form = TaskForm()
    return render(request, 'todoapp/create_task.html', {'form': form})
