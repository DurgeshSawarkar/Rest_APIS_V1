from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def students(request):
    return HttpResponse("<h1> Rest framework </h1>")