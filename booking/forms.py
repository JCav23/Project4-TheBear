from django import forms
from .models import Booking
import datetime


class DateInput(forms.DateInput):
    """
    Provides the user with a UI Calendar to select date
    entry.
    """
    input_type = 'date'


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
        labels = {
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'date': 'Date',
            'time': 'Time',
            'num_guests': 'Number Of Guests',
            'contact_number': 'Contact Number',
        }
        widgets = {
            'date': DateInput()
        }
