from django.urls import path
from . import views

app_names = 'pizzas'
urlpatterns = [
    path('', views.index, name='index'),
]