from . import views
from django.urls import path


urlpatterns = [
    path('form/', views.book_table, name='book_table'),
    path('bookings/', views.view_booking, name='view_booking'),
    path(
        'bookings/delete/<int:booking_id>',
        views.delete_booking,
        name='delete_booking'),
    path(
        'bookings/update/<int:booking_id>/',
        views.update_booking,
        name='update_booking'),

]