from django.shortcuts import render
from django.shortcuts import render,redirect
from  django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.
import request


def home_view(request,*args,**kwargs):
    return render(request, 'firstapp/home.html', {})

def food_details(request, *args):
    chappati = request.POST.get('chappati')
    rice = request.POST.get('rice')
    dal = request.POST.get('dal')
    veges = request.POST.get('veges')
    sweet = request.POST.get('sweet')
    uname = request.session['username']
    mess = Mess.object.exclude(username != uname)
    hostel = mess[0]
    new_food = FoodDetails(mess=hostel,roti=chappati,rice=rice,dal=dal,sabji=veges,sweet=sweet)
    new_food.save()
