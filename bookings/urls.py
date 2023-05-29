from . import views
from django.urls import path


urlpatterns = [
    path('form/', views.book_table, name='book_table'),
    path('bookings/<int:pk>/', views.view_booking, name='view_booking'),
]