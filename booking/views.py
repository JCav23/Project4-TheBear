from django.shortcuts import render
from django.contrib import messages
from .forms import BookingForm
from .models import Booking

# Create your views here.
def create_booking(request):
    """
    Renders the Create Booking Page
    """
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.guest = request.user
            booking.save()
            messages.add_message(
                request, 
                messages.SUCCESS,
                "Booking Confirmed")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors)
    form = BookingForm()
    return render(
        request,
        "bookings/create_booking.html",
        {'booking_form': form}
    )


def reservations(request):
    """ The View that renders the reservations.html
    which shows all bookings made by the current user
    or gives link to make a booking if no reservations made
    or redirects to signup page if user is not signed in.
    """
    bookings = Booking.objects.filter(guest=request.user).order_by('-date')
    context = {
        'bookings': bookings
    }
    return render(request, 'bookings/reservations.html', context)
