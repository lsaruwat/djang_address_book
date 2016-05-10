#Logan Saratuwari, Charles Bisbee, Zach Lovergne
#This is a django web application designed to function as an address book
#There is functionality to add, view, create, edit, and sort contacts
#This .py file creates the model for each contact

from django.db import models

# Create your models here.

class Student(models.Model):
	
	first_name = models.CharField(max_length =50)
	last_name = models.CharField(max_length =50)
	email = models.CharField(max_length =50)
	phone = models.CharField(max_length =50)

	def __str__(self):

		return self.first_name + " " + self.last_name
