from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Mess)
admin.site.register(Mess_location)
admin.site.register(NGO)
admin.site.register(NGO_location)
admin.site.register(FoodDetails)
admin.site.register(Results)
admin.site.register(MealCount)
admin.site.register(DummyModel)