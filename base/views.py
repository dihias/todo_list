import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
 
#creating asimple funtional view to test my app
def tasklist(request):
    return HttpResponse('to do list')

