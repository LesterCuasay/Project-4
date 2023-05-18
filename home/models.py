from django.db import models
from django.views.generic import CreateView
from .forms import LogInForm


class LogIn(CreateView):
    model = get_user_model()
    form = LogInForm
    template_name = 'accounts/login.html'
