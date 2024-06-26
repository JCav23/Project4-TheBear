from . import views
from django.urls import path


urlpatterns = [
    path('new_booking/', views.create_booking, name='create_booking'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/delete/<booking_id>', views.delete_reservation, name='delete'),
    path('reservations/edit/<booking_id>', views.edit_reservation, name='edit')
]