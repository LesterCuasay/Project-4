from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/index.html')


class Menu(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/menu.html')
