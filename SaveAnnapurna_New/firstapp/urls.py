"""sos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import *

from firstapp.views import *

app_name = 'firstapp'

urlpatterns = [
    path('', home_view, name="home"),
    path('food_details/',food_details_view),
    path('mess_login/',mess_login_attempt),
path('ngo_login/',ngo_login_attempt),
path('mess_signup/',mess_signup_attempt),
path('ngo_signup/',ngo_signup_attempt),
    path('mess_signup_data/',mess_register),
path('ngo_signup_data/',ngo_register),
path('stu_signup_data/',student_register),
path('login/',mess_login,name="login"),
path('login_stu/',student_login,name="login_stu"),
path('login_ngo/',ngo_login,name="login_ngo"),
    path('stu_login/',stu_login_attempt),
path('stu_signup/',stu_signup_attempt),
    path('logout/',logout),
    path('mess_details/',main_view),
    path('meal_detail/',meal_count),
    path('email/',Email_View),
  #  path('/login_student/',student_login_view),
  #  path('/signup_student/',register_student)
]



