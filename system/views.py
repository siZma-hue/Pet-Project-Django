from .models import Category
from .models import Dish
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    qs = Dish.objects.all()
    return render(request, 'system/index.html', {'dishes': qs})



def dine_in(request):
    return HttpResponse('<h2>В заведении</h2>')

def pickup_order(request):
    return HttpResponse('<h2>С собой</h2>')

def delivery_order(request):
    return HttpResponse('<h2>Доставка</h2>')

