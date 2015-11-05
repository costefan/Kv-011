# coding: utf-8
from django.conf.urls import patterns, url

__author__ = 'mironnn'

urlpatterns = patterns('plan_viewer.views',
                       url(r'^$', 'show_map', name='show_map'),
                       )