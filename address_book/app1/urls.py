from django.conf.urls import url

from . imort views

urlpatterns = [
	url(r'^admin/', views.index, name='index'),
]