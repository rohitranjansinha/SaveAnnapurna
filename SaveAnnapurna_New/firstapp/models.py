from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=1000)
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
    phone = models.CharField(max_length=12)

class NGO_location(models.Model):
    username = models.CharField(max_length=60)
    ngo_lat = models.CharField(max_length=1000)
    ngo_lon = models.CharField(max_length=100)




