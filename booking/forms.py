from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'f_name',
            'l_name',
            'date',
            'time',
            'num_guests',
            'contact_number',
        )