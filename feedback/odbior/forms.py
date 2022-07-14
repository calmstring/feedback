#from email import utils
from django.forms import ModelForm
from .models import zgloszenie
from django.utils import timezone

class ZgloszenieForm(ModelForm):
    class Meta:
        model = zgloszenie
        fields = ['tekst','nazwa_autora']
