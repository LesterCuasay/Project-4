from django.shortcuts import render, redirect
from django.views import View


class Menu(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/menu.html')
