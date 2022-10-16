from django.shortcuts import render

from .models import Task
# Create your views here.

def home(request, *args, **kwargs):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'home.html', context)

def detail(request, pk, *args, **kwargs):
    task = Task.objects.get(pk=pk)
    context = {"task": task}
    return render(request, 'detail.html', context)
