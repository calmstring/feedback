from django.urls import path

from . import views

app_name = 'odbior'
urlpatterns = [
    path('', views.index, name='index'),
    path('odpowiedz/', views.odpowiedz, name='odpowiedz'),
]