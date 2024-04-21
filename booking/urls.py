from . import views
from django.urls import path

urlpatterns = [
    path('book-a-table/', views.create_booking, name='create_booking'),
]