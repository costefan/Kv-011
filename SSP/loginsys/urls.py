__author__ = 'costefan'
from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^login/$', 'loginsys.views.login', name='login'),
    url(r'^logout/$', 'loginsys.views.logout', name='logout'),
]