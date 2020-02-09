from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def business(request):
    return HttpResponse("Hello business")
