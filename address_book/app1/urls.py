from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/$', views.home, name='home'),
	url(r'^insertUser/$', views.insertUser, name='insertUser'),
	url(r'^deleteUser/$', views.deleteUser, name='deleteUser'),
	url(r'^updateUser/$', views.updateUser, name='updateUser'),
	url(r'^searchUser/$', views.searchUser, name='searchUser'),
	url(r'^template/$', views.template, name='template'),
	url(r'^viewAll/$', views.viewAll, name='viewAll'),
]