from django.shortcuts import render
from django.shortcuts import render,redirect
from  django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.



def home_view(request,*args,**kwargs):
    return render(request, 'firstapp/home.html', {})