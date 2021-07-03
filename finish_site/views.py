from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    return render(request, "finish_site/index.html")

def welcom (request):
    return HttpResponse ("<h1>Вы зарегистрированы. Добро пожаловать!</h1>")
