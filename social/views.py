""" imports render """
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.views import View
# Create your views here.
from django.views import generic
from django.urls import reverse,reverse_lazy
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def index(request):
    """ Index Page:
        if logged in
            return Homepage
        else
            Login/SignUp Page """

    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['pass']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return HttpResponse('login not successfull')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return render(request,'social/homepage.html')
        return render(request, 'social/index.html')

def signup(request):
    """ SignUp controller:
        requires name & password"""
    user = User.objects.create_user(
        request.POST['name'],
        request.POST['email'],
        request.POST['pass']
        )
    user.save()
    return HttpResponseRedirect(reverse('index'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))