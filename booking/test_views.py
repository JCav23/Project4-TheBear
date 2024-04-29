from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Booking
from .forms import BookingForm

# Create your tests here.
class TestBookingViews(TestCase):

    def setUp(self):
        """
        Creates Mock User & Data for testing purposes
        """
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
        """
        Mocks login using test user and checks render of reservation
        of mock booking
        """
        self.client.login(username='Mrtest', password='TestyTesterTesting')
        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tim', response.content)
        self.assertIn(b'19:00', response.content)
    
