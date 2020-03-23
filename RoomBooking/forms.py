from django.forms import ModelForm
from .models import *

class BookingForm(ModelForm):
    class Meta:
        model=Guest
        fields='__all__'

class SlotsForm(ModelForm):
    class Meta:
        model=Available
        fields='__all__'
