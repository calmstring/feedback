from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import zgloszenie
from django.utils import timezone
from .forms import ZgloszenieForm

# Create your views here.

def index(request):
    return HttpResponse("czesc")

def odpowiedz(request):
    a = ZgloszenieForm()
    if request.method == 'POST':
        a = ZgloszenieForm(request.POST)

        if a.is_valid(): 
         a.save()

    context = {'a':a}

    return render(request, "odbior/odpowiedz.html", context)
