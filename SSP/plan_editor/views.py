# coding: utf-8

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
__author__ = 'mironnn'


@login_required(login_url='/auth/login/')
def index(request):
    return render(request, "index.html")


def show_map(request):
    return render(request, "office_map.html")
    # return HttpResponse('ok')