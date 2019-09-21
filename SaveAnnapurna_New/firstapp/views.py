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
    mess = Mess.objects.filter(username = uname)
    hostel = mess[0]
    new_food = FoodDetails(mess=hostel,roti=chappati,rice=rice,dal=dal,sabji=veges,sweet=sweet)
    new_food.save()
    return HttpResponseRedirect(reverse('firstapp:login'))

def mess_login_attempt(request):
    return render(request, 'firstapp/signin_mess.html', {})

def stu_login_attempt(request):
    return render(request, 'firstapp/signin_student.html', {})

def mess_signup_attempt(request):
    return render(request, 'firstapp/signup_mess.html', {})

def stu_signup_attempt(request):
    return render(request, 'firstapp/signup_student.html', {})

def mess_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    mess_na = request.POST.get('mess_number')
    emal = request.POST.get('email')
    obj = Mess(username=username,password=password,email=emal,mess_name=mess_na)
    obj.save();
    return render(request, 'firstapp/home.html', {})

def student_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    mess_na = request.POST.get('mess_number')
    emal = request.POST.get('email')
    obj = Student(username=username,password=password,email=emal,mess_name=mess_na)
    obj.save();
    return render(request, 'firstapp/home.html', {})

def mess_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if (username != None and password != None):
        request.session['username'] = username
        request.session['password'] = password
        request.session['data'] = None
    else:
        username = request.session['username']
        password = request.session['password']
    test = Mess.objects.filter(username=username).filter(password=password)
    print('AJAX')
    if (test):
        context = {
            'user': test[0],
            'data': request.session['data'],
        }

        print('Valid User')
        test2 = test[0]
        print(type(test2))
        if(request.session['data'] != None):
           context['data'] = request.session['data']
        return render(request, 'firstapp/profile_mess.html', context)
    else:
        print('Invalid User')
        return HttpResponseRedirect(reverse('firstapp:home'))

def student_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if (username != None and password != None):
        request.session['username'] = username
        request.session['password'] = password
        request.session['data'] = None
    else:
        username = request.session['username']
        password = request.session['password']
    test = Student.objects.filter(username=username).filter(password=password)
    print('AJAX')
    if (test):
        context = {
            'user': test[0],
            'data': request.session['data'],
        }

        print('Valid User')
        test2 = test[0]
        print(type(test2))
        if(request.session['data'] != None):
           context['data'] = request.session['data']
        return render(request, 'firstapp/profile_student.html', context)
    else:
        print('Invalid User')
        return HttpResponseRedirect(reverse('firstapp:home'))