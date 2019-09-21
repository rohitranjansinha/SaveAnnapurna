from django.shortcuts import render
from django.shortcuts import render,redirect
from  django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.
import request
import requests

#Making JSON encoder
from json import JSONEncoder
import json
class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__




def logout(request):
    request.session['username'] = None
    request.session['password'] = None
    request.session['data'] = None
    return render(request, 'firstapp/home.html', {})

def home_view(request,*args,**kwargs):
    return render(request, 'firstapp/home.html', {})

def food_details_view(request, *args):
    chappati = request.POST.get('chappati')
    rice = request.POST.get('rice')
    dal = request.POST.get('dal')
    veges = request.POST.get('veges')
    sweet = request.POST.get('sweet')
    username = request.session['username']

    coord = request.POST.get('loc')
    test = str(coord).split(',')
    ob = Mess_location.objects.filter(username=username)
    if (len(ob) == 0):
        obj = Mess_location(username=username, mess_lat=test[0], mess_lon=test[1])
        obj.save()
    else:
        obj = ob[0]
        obj.mess_lat = test[0]
        obj.mess_lon = test[1]
        obj.save()
    mess = Mess.objects.filter(username = username)
    hostel = mess[0]
    new_food = FoodDetails(mess=hostel.username,roti=chappati,rice=rice,dal=dal,sabji=veges,sweet=sweet)
    new_food.save()
    return HttpResponseRedirect(reverse('firstapp:login'))

def mess_login_attempt(request):
    return render(request, 'firstapp/signin_mess.html', {})

def stu_login_attempt(request):
    return render(request, 'firstapp/signin_student.html', {})

def ngo_login_attempt(request):
    return render(request, 'firstapp/signin_ngo.html', {})

def mess_signup_attempt(request):
    return render(request, 'firstapp/signup_mess.html', {})

def stu_signup_attempt(request):
    return render(request, 'firstapp/signup_student.html', {})

def ngo_signup_attempt(request):
    return render(request, 'firstapp/signup_ngo.html', {})

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

def ngo_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    #mess_na = request.POST.get('mess_number')
    emal = request.POST.get('email')
    obj = NGO(username=username,password=password,email=emal)
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

def ngo_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if (username != None and password != None):
        request.session['username'] = username
        request.session['password'] = password
        request.session['data'] = None
    else:
        username = request.session['username']
        password = request.session['password']
    test = NGO.objects.filter(username=username).filter(password=password)
    #print('AJAX')
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
        return render(request, 'firstapp/profile_ngo.html', context)
    else:
        print('Invalid User')
        return HttpResponseRedirect(reverse('firstapp:home'))


def main_view(request):
    location = request.POST.get('location')
    url2 = '&mode=fastest;car;traffic:disabled'
    url = url = 'https://route.api.here.com/routing/7.2/calculateroute.json?app_id=9Ab1yIULBo3Lj9plEA8t&app_code=JhmMlH2uPy4UEH5ShcXnMQ&waypoint0=geo!'+location+'&waypoint1=geo!'
    mess = FoodDetails.objects.all()
    final_list = list()
    for obj in mess:
        add = Mess_location.objects.filter(username=obj.mess)
        new_ob = Results(mess = add[0].username,location=add[0].mess_lat+','+add[0].mess_lon,)
        final_list.append(new_ob)
        new_url = url + (add[0].mess_lat+','+add[0].mess_lon) + url2
        response = requests.get(new_url)
        data = response.json()
        dis = data['response']['route'][0]['summary']['distance']
        dur = data['response']['route'][0]['summary']['baseTime']
        print('dis = ', dis)
        print('dur = ', dur)
        final_list[-1].distance = (float)(dis / 1000.0)
        final_list[-1].time = (float)(dur / 3600.0)
    final_list.sort(key=lambda x: x.distance, reverse=False)
    for i in range(len(final_list)):
        final_list[i] = json.dumps(final_list[i], cls=MyEncoder)
    for i in range(len(final_list)):
        final_list[i] = json.loads(final_list[i])
    request.session['data'] = final_list
    return HttpResponseRedirect(reverse('firstapp:login_ngo'))

