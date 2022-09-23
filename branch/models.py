from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

# phone validator using regular expressions
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Phone number invalid. Should start with example: +233'
)


class Branch(models.Model):
    ''' Manages bank branche information'''
    name = models.CharField(max_length=100, unique=True)
    opening_date = models.DateField()
    country = models.CharField(max_length=50)
    COUNTY = (
        ('Nairobi', 'Nairobi'),
        ('Uasin Gishu', 'Uasin Gishu'),
        ('Bomet','Bomet'),
        ('Kericho', 'Kericho'),
        ('West Pokot','West Pokot'),
        ('Siaya', 'Siaya'),
        ('Nakuru', 'Nakuru'),
        ('Kiambu', 'Kiambu'),
        ('Kajiado', 'Kajiado'),
        ('Taita Taveta', 'Taita Taveta'),
        ('Elgeiyo Marakwet', 'Elgeiyo Marakwet'),
        ('Samburu', 'Samburu' ),
        ('Kisii', 'Kisii'),
        ('Narok', 'Narok'),
        ('Mombasa', 'Mombasa'),
        ('Baringo', 'Baringo'),
        ('Kwale', 'Kwale'),
        ('Kilifi', 'Kilifi'),
        ('Tana River', 'Tana River'),
        ('Lamu', 'Lamu'),
        ('Garrissa', 'Garrissa'),
        ('Marsabit', 'Marsabit'),
        ('Mandera', 'Mandera'),
        ('Isiolo', 'Isiolo'),
        ('Meru', 'Meru'),
        ('Tharaka-Nithi', 'Tharaka-Nithi'),
        ('Kitui', 'Kitui'),
        ('Embu', 'Embu'),
        ('Machakos', 'Machakos'),
        ('Makueni', 'Makueni'),
        ('Nyandarua', 'Nyandarua'),
        ('Nyeri', 'Nyeri'),
        ('Kirinyaga', 'Kirinyaga'),
        ('Muranga', 'Muranga'),
        ('Turkana', 'Turkana'),
        ('Trans-Nzoia', 'Trans-Nzoia'),
        ('Nandi', 'Nandi'),
        ('Laikipia', 'Laikipia'),
        ('Kakamega', 'Kakamega'),
        ('Vihiga', 'Vihiga'),
        ('Bungoma', 'Bungoma'),
        ('Busia', 'Busia'),
        ('Kisumu', 'Kisumu'),
        ('Migori', 'Migori'),
        ('Kisii', 'Kisii'),
        ('Nyamira', 'Nyamira'), 
        ('Homabay', 'Homabay'),
    )
    county = models.CharField(max_length=20, choices=COUNTY)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[phone_regex], max_length=12)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('branch:branch_list')

    class Meta:
        verbose_name = 'Branch Name'
        verbose_name_plural = 'Branch Names'
