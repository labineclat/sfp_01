from django.conf.urls import patterns, url, include
from itemlist import views

urlpatterns=[
	url(r'^$', views.index, name='index')
]