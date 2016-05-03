from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^home/$', views.home, name='home'),
	url(r'^deleteUser/$', views.deleteUser, name='deleteUser'),
	url(r'^updateUser/$', views.updateUser, name='updateUser'),
	url(r'^saveUser/([0-9]*)', views.saveUser, name='saveUser'),
	url(r'^searchUser/$', views.searchUser, name='searchUser'),
	url(r'^template/$', views.template, name='template'),
	url(r'^viewAll/$', views.viewAll, name='viewAll'),
	url(r'^addUser/([0-9]*)', views.addUser, name='addUser'),
]


