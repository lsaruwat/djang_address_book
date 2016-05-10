#Logan Saratuwari, Charles Bisbee, Zach Lovergne
#This is a django web application designed to function as an address book
#There is functionality to add, view, create, edit, and sort contacts
#This .py file manages all of the url's for the project

from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^home/$', views.home, name='home'),
	url(r'^deleteUser/$', views.deleteUser, name='deleteUser'),
	url(r'^updateUser/$', views.updateUser, name='updateUser'),
	url(r'^saveUser/([0-9]*)', views.saveUser, name='saveUser'),
	url(r'^delete/([0-9]*)', views.delete, name='delete'),
	url(r'^searchUser/$', views.searchUser, name='searchUser'),
	url(r'^search/$', views.search, name='search'),
	url(r'^template/$', views.template, name='template'),
	url(r'^viewAll/$', views.viewAll, name='viewAll'),
	url(r'^viewAllFirstName/$', views.viewAllFirstName, name='viewAllFirstName'),
	url(r'^viewAllLastName/$', views.viewAllLastName, name='viewAllLastName'),
	url(r'^viewAllPhone/$', views.viewAllPhone, name='viewAllPhone'),
	url(r'^viewAllEmail/$', views.viewAllEmail, name='viewAllEmail'),
	url(r'^addUser/([0-9]*)', views.addUser, name='addUser'),
	url(r'^login/$', views.loginPage, name='loginPage'),
	url(r'^logoutThing/$', views.logoutThing, name='logoutThing'),
	url(r'^verify/$', views.verifyCredentials, name='verify'),
]


