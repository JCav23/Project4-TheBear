from . import views as home_views
from booking import views as booking_views
from django.urls import path

urlpatterns = [
    path('', home_views.homepage, name='home'),
    path('reservations/', booking_views.reservations, name='redirect_reservations')
]