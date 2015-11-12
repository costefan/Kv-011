from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


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
    auth.logout(request)  # delete this session
    return redirect('/')
