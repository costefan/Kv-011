# coding: utf-8

from django.shortcuts import render

__author__ = 'mironnn'


def index(request):
    return render(request, "index.html")