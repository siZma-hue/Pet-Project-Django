from .models import Category, HomePage
from .models import Dish
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    hp = HomePage.objects.all()
    return render(request, 'system/index.html', {'homepage': hp})

def menu(request):
    qs = Dish.objects.all()
    return render(request, 'system/menu.html', {'dishes': qs})


def dine_in(request):
    return HttpResponse('<h2>У закладі</h2>')

def pickup_order(request):
    return HttpResponse('<h2>З собою</h2>')

def delivery_order(request):
    return HttpResponse('<h2>Доставка</h2>')

