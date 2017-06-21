from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^add_course$', views.add_course),
	url(r'^delete_course/(?P<id>\d+$)', views.delete_course),
	url(r'^confirm_delete/(?P<id>\d+$)', views.confirm_delete),
	url(r'^cancel_delete$', views.cancel_delete)
]
