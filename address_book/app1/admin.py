#Logan Saratuwari, Charles Bisbee, Zach Lovergne
#This is a django web application designed to function as an address book
#There is functionality to add, view, create, edit, and sort contacts
#This .py file manages the admin page for the application

from django.contrib import admin

# Register your models here.
from .models import Student

admin.site.register(Student)