from django.shortcuts import render
from django.http import HttpResponse


def HomeView(request):
    return render(request, 'home/home.html')
