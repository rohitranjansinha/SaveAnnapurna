from django.db import models

# Create your models here.
import datetime

class Student(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=1000)
    mess_name = models.CharField(max_length=100)
    email = models.EmailField()

class Mess(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=1000)
    email = models.EmailField()
    mess_name = models.CharField(max_length=100)

class Mess_location(models.Model):
    username = models.CharField(max_length=60)
    mess_lat = models.CharField(max_length=1000)
    mess_lon = models.CharField(max_length=1000)

class NGO(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=1000)
    ngo_name = models.CharField(max_length=100)
    email = models.EmailField()


class NGO_location(models.Model):
    username = models.CharField(max_length=60)
    ngo_lat = models.CharField(max_length=1000)
    ngo_lon = models.CharField(max_length=100)

class FoodDetails(models.Model):
    mess = models.CharField(max_length=60)
    roti = models.CharField(max_length=10)
    rice = models.CharField(max_length=10)
    dal = models.CharField(max_length=10)
    sabji = models.CharField(max_length=10)
    sweet = models.CharField(max_length=10)

class Results(models.Model):
    mess = models.CharField(max_length=60)
    location = models.CharField(max_length=1000)
    distance = models.DecimalField(null=True, max_digits=100, decimal_places=100)
    time = models.DecimalField(null=True, max_digits=100, decimal_places=100)

class MealCount(models.Model):
    mess = models.CharField(max_length=60)
    breakfast = models.IntegerField(null=True, default=0)
    lunch = models.IntegerField(null=True, default=0)
    dinner = models.IntegerField(null=True, default=0)

class DummyModel(models.Model):
    lunch_end = models.IntegerField(default=11)
    breakfast_end = models.IntegerField(default=7)
    dinner_end = models.IntegerField(default=18)
    def isBreakfast(self):
        return ((datetime.datetime.now().hour)<7)
    def isLunch(self):
        return ((datetime.datetime.now().hour)<11)
    def isDinner(self):
        return ((datetime.datetime.now().hour)<18)
