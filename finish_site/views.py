
from django.shortcuts import render
from .models import Task
from django.forms.forms import Form
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index (request):
    tasks = Task.objects.all()
    return render(request, "finish_site/index.html", {'title': 'Главная страница сайта', 'tasks': tasks})

def welcom (request):
    return render(request, "finish_site/welcom.html")   #, {'title': 'Главная страница сайта', 'tasks': tasks})


