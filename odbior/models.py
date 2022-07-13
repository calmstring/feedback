from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class zgloszenie(models.Model):
     tekst = models.CharField(max_length=200)
     nazwa_autora = models.CharField(max_length=200)
     data_publikacji = models.DateTimeField('data publikacji', default=timezone.now())