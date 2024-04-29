from django.test import TestCase
from .forms import BookingForm

# Create your tests here.
class TestBookingForm(TestCase):
    """
    Test suite for testing the booking form validation
    """

    def test_form_is_valid(self):
        """
        Tests validition on entire form
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2024-05-25',
            'time': '19:00',
            'num_guests': '2',
            'contact_number': '12345678',
        })
        self.assertTrue(booking_form.is_valid())


    def test_form_f_name_field(self):
        """
        Tests validition on first name field using empty field
        """
        booking_form = BookingForm({
            'f_name': '',
            'l_name': 'test',
            'date': '2024-04-27',
            'time': '19:00',
            'num_guests': '2',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())


    def test_form_l_name_field(self):
        """
        Tests validition on last name field using empty field
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': '',
            'date': '2024-04-27',
            'time': '19:00',
            'num_guests': '2',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())


    def test_form_date_field(self):
        """
        Tests validition on date field using empty field
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '',
            'time': '19:00',
            'num_guests': '2',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())

    
    def test_form_date_field_wrong_format(self):
        """
        Tests validition on date field using incorrect format dd-mm-yyyy
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '23-02-2025',
            'time': '19:00',
            'num_guests': '2',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())


    def test_form_date_field_past_date(self):
        """
        Tests validition on date field using date in the past
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2025-02-1994',
            'time': '19:00',
            'num_guests': '2',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())

    
    def test_form_time_field(self):
        """
        Tests validition on time field using empty field
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2024-04-27',
            'time': '',
            'num_guests': '2',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())

    
    def test_form_time_field_closed_hours(self):
        """
        Tests validition on time field using time outside of opening hours
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2024-04-27',
            'time': '08:00',
            'num_guests': '2',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())


    def test_form_time_field_wrong_format(self):
        """
        Tests validition on time field using time outside of 24 hour clock
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2024-04-27',
            'time': '28:00',
            'num_guests': '2',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())

    
    def test_form_num_guests_field(self):
        """
        Tests validition on number of guests field using empty field
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2024-04-27',
            'time': '28:00',
            'num_guests': '',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())


    def test_form_num_guests_field_no_guests(self):
        """
        Tests validition on number of guests field using zero
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2024-04-27',
            'time': '28:00',
            'num_guests': '0',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())


    def test_form_num_guests_field_too_many_guests(self):
        """
        Tests validition on number of guests field using number bigger than largest accepted sitting
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2024-04-27',
            'time': '28:00',
            'num_guests': '11',
            'contact_number': '12345678',
        })
        self.assertFalse(booking_form.is_valid())


    def test_form_contact_number(self):
        """
        Tests validition on contact number field using empty field
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2024-04-27',
            'time': '28:00',
            'num_guests': '11',
            'contact_number': '',
        })
        self.assertFalse(booking_form.is_valid())


    def test_form_contact_number_wrong_format(self):
        """
        Tests validition on contact number field using text
        """
        booking_form = BookingForm({
            'f_name': 'mr',
            'l_name': 'test',
            'date': '2024-04-27',
            'time': '28:00',
            'num_guests': '11',
            'contact_number': 'contact',
        })
        self.assertFalse(booking_form.is_valid())