from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Booking
from .forms import BookingForm

# Create your tests here.
class TestBookingViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="Mrtest",
            password="TestyTesterTesting",
            email="test@test.com"
        )
        self.booking = Booking(
            guest= self.user,
            f_name='Tim',
            l_name='Esting',
            date='2024-06-23',
            time='19:00',
            num_guests='2',
            contact_number='123456789'
        )
        self.booking.save()


    def test_render_reservations(self):
        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tim', response.content)
        self.assertIn(b'123456789', response.content)
    
