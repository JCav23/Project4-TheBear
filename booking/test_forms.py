from django.test import TestCase
from .forms import BookingForm

# Create your tests here.
class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2024-04-27',
            'time': '19:00',
            'num_guests': '2',
            'contact_number': '12345678',
        })
        self.assertTrue(booking_form.is_valid())