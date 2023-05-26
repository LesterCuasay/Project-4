from . import views
from django.urls import path


urlpatterns = [
    path('form', views.book_table, name='form'),
]