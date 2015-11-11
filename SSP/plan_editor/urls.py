# coding: utf-8
from django.conf.urls import patterns, url

__author__ = 'mironnn'

urlpatterns = patterns('SSP.plan_editor.views',
                       url(r'^$', 'show_map', name='show_map'),
                       )