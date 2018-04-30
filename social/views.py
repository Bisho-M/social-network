""" imports render """
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.views import View
# Create your views here.
from django.views import generic
from django.urls import reverse,reverse_lazy
from .models import Post