from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import datetime

HOURS = (
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),
)

GUESTS = (
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
)

def validate_date(date):
    if date < datetime.date.today():
            raise ValidationError(
                "The Date cannot be in the Past!",
                params={"date": date},
            )
    if date.weekday() == 6:
            raise ValidationError(
                "Sorry, We Are Closed on Sundays!",
                params={"date": date},
            )

# Create your models here.
class Booking(models.Model):
    """
    Model to store a guest's booking information entered into 
    the booking form when creating a booking. Guest uses Foreign
    key constraint to relate each booking to specific user. 
    """

    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='guest_booking'
    )
    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=20)
    date = models.DateField(
        validators=[validate_date]
    )
    time = models.CharField(choices=HOURS, default='19:00', max_length=10)
    num_guests = models.IntegerField(choices=GUESTS, default='4')
    phoneValidate = RegexValidator(
        regex=r'^\+?1?\d{8,15}$',
        message='Please enter valid contact number,'
        'digits only, up to 15 allowed.',
        code="invalid"
    )
    contact_number = models.CharField(
        validators=[phoneValidate],
        max_length=16
    )
    
    class Meta:
        ordering = ['-time','-date']
        unique_together = ('date', 'time', 'guest')

    def __str__(self):
        return f"Booking for {self.f_name} {self.l_name} at {self.date} at {self.time}"
