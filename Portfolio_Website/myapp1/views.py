from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def land_view(request):
    return render(request, 'landing.html')

def home_view(request):
    return render(request, 'home.html')
