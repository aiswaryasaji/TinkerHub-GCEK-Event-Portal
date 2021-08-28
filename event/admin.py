from django.contrib import admin

# Register your models here.
from .models import Event, Student


admin.site.register(Event)
admin.site.register(Student)
