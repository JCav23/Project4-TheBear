# Generated by Django 4.2.11 on 2024-04-21 13:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=15)),
                ('l_name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField(choices=[('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00')], default='19:00')),
                ('num_guests', models.IntegerField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='4')),
                ('contact_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(code='invalid', message='Please enter valid contact number,digits only, up to 15 allowed.', regex='^\\\\+?[1-9][0-9]{8,15}$')])),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('date', 'time', 'guest')},
            },
        ),
    ]
