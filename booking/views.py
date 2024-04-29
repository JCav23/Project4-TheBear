from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BookingForm
from .models import Booking


# Create your views here.
def create_booking(request):
    """
    Renders the Create Booking Page, presents the user
    with a form and validation to submit details for
    desired booking for the guest.
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
                "Booking Confirmed, We Look Forward to Seeing you")
            return redirect('reservations')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                list(form.errors.values())[0])
    form = BookingForm()
    return render(
        request,
        "bookings/create_booking.html",
        {'booking_form': form}
    )


def reservations(request):
    """
    The View that renders the reservations.html
    which shows all bookings made by the current user
    or gives link to make a booking if no reservations made
    or redirects to signup page if user is not signed in.
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(
            guest=request.user.id).order_by('-date')
        context = {
            'bookings': bookings
        }
        return render(request, 'bookings/reservations.html', context)
    else:
        return redirect('/accounts/login')


def delete_reservation(request, booking_id):
    """
    The View that deletes the desired boooking, requires the
    user that made the booking otherwise will redirect back
    to reservations.
    """
    reservation = get_object_or_404(Booking, pk=booking_id)
    if request.user == reservation.guest:
        reservation.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Your reservation has been cancelled."
        )
        return redirect('reservations')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "ERROR: Only the Guest who made the reservation has permission to cancel."
        )
        return redirect('reservations')


def edit_reservation(request, booking_id):
    """
    The view for editing a currently existing booking, validates the current user
    or redirects back to reservations. Autofills form with current data stored
    in the booking.
    """
    reservation = get_object_or_404(Booking, pk=booking_id)
    if request.user == reservation.guest:
        if request.method == 'POST':
            form = BookingForm(data=request.POST, instance=reservation)
            if form.is_valid():
                reservation.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Booking Updated. See you soon!")
                return redirect('reservations')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    list(form.errors.values())[0])
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "ERROR: Only the Guest who made the reservation has permission to change a reservation."
        )
        return redirect('reservations')
    form = BookingForm(instance=reservation)
    return render(
        request,
        "bookings/edit_booking.html",
        {'booking_form': form}
    )
