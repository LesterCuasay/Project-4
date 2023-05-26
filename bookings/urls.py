from . import views
from django.urls import path


urlpatterns = [
    path('form', views.book_table, name='form'),
    path('my-bookings', views.book_list, name='booking_list'),

]