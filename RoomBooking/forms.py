from django.forms import ModelForm
from .models import *

class BookingForm(ModelForm):
    class Meta:
        model=Guest
        exclude=['user']

class SlotsForm(ModelForm):
    class Meta:
        model=Available
        fields='__all__'
