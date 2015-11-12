# coding: utf-8

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
__author__ = 'mironnn'


@login_required(login_url='/login/')
def index(request):
    return render(request, "index.html")


@login_required(login_url='/login/')
def show_map(request):
    return render(request, "office_map.html")
    # return HttpResponse('ok')


def login(request):
    """
    user login method
    :param request
    :return: render or redirect that depends on authentication
    """
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # create session
            return redirect('/')
        else:
            args['login_error'] = 'Cannot find the user'  # to show error in form
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    """
    user logout on system
    :param request:
    :return:
    """
    auth.logout(request)  # delete this session
    return redirect('/')
