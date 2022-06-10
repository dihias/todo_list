from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Task

# Create your views here.
 
#creating the list view as a class
class TaskList(ListView):
   model = Task

