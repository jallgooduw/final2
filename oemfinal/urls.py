from django.conf.urls import patterns, url
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from oemfinal import views

urlpatterns = [
    url(r'^$', views.device_list, name='device_list'),
    url(r'^device/$', views.device_list),
    url(r'^devices/$', views.device_list),
    url(r'^deviceapi/$', views.device_listAPI),
    url(r'^device/(?P<pk>[0-9]+)/$', views.device_detail, name='device_detail'),
    url(r'^device/new/$', views.device_new, name='device_new'),
    url(r'^device/(?P<pk>[0-9]+)/edit/$', views.device_edit, name='device_edit'),
]

urlpatterns = format_suffix_patterns(urlpatterns)