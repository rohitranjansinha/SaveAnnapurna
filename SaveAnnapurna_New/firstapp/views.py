from django.shortcuts import render
from django.shortcuts import render,redirect
from  django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.
import request


def home_view(request,*args,**kwargs):
    return render(request, 'firstapp/home.html', {})

def food_details_view(request, *args):
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
    return HttpResponseRedirect(reverse('firstapp:login'))

def mess_login_attempt(request):
    return render(request, 'firstapp/signin_mess.html', {})

def mess_signup_attempt(request):
    return render(request, 'firstapp/signup_mess.html', {})

def mess_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    mess_na = request.POST.get('mess_number')
    emal = request.POST.get('email')
    obj = Mess(username=username,password=password,email=emal,mess_name=mess_na)
    obj.save();
    return render(request, 'firstapp/home.html', {})

