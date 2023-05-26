from . import views
from django.urls import path


urlpatterns = [
    path('form', views.BookTable, name='form'),
]