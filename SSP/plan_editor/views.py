# coding: utf-8

from django.shortcuts import render, HttpResponse

__author__ = 'mironnn'


def index(request):
    return render(request, "index.html")


def show_map(request):
    return render(request, "office_map.html")
    # return HttpResponse('ok')