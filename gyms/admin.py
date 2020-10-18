from django.contrib import admin

# Register your models here.
from .models import Gym,Class,Booking,Profile

admin.site.register(Gym)
admin.site.register(Class)
admin.site.register(Booking)
# admin.site.register(GymUser)
admin.site.register(Profile)
