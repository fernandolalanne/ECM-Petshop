from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator

# Create your models here.

class Pets(models.Model):
    sold_choices = [('No', 'No'), ('Yes', 'Yes')]
    LOCATION_CHOICES = [
        ('Location1', 'Location 1'),
        ('Location2', 'Location 2'),
        ('Location3', 'Location 3'),
        ('Location4', 'Location 4'),
    ]
    name_validator = RegexValidator(regex=r'^[a-zA-Z ]*$', message='Only letters are allowed.')

    name = models.CharField(max_length=220, null=True, validators=[name_validator])
    price = models.FloatField(default=0.0)
    description = models.TextField(verbose_name='Description', null=True)
    digital = models.BooleanField(default=True, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)
    sold = models.CharField(max_length=3, choices=sold_choices, default='No', null=True, blank=False)
    hungry = models.CharField(max_length=3, choices=sold_choices, default='No', null=True, blank=False)
    location = models.CharField(max_length=40, choices=LOCATION_CHOICES, default='Location1', null=True, blank=False)

    
    def sell_pet(self):
        self.sold = 'Yes'
        self.save()
    
    def __str__(self):
        fila = "Name: " + self.name
        return fila
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
     

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    formateur = models.OneToOneField(Pets, on_delete=models.CASCADE)

class UploadFileForm(forms.Form):
    excel_file = forms.FileField()

class CartItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Otros campos que puedas necesitar

    def __str__(self):
        return self.name