from django.shortcuts import render
from django.contrib import messages
from .forms import BookingForm

# Create your views here.
def create_booking(request):
    """
    Renders the Create Booking Page
    """

    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking_form.user = request.user
            messages.success(request, 
            "Your booking has been confirmed, we look forward to seeing you.")
        else:
            messages.error(
                request, "Error: Booking is Unavailable or Invalid"
            )

    booking_form = BookingForm()

    return render(
        request,
        "bookings/create_booking.html",
        {
            "booking_form": booking_form,
        },
    )