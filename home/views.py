from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import generic

# Create your views here.


def home(request):
    return render(request, 'base.html')
