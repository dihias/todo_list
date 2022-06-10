import imp
from django.shortcuts import render

from django.views.generic.detail import DetailView
from .models import Task
# Create your views here.

class TaskDetail(DetailView):
    model = Task

    #edit the template name from the default task_detail to task
    template_name = 'base/task.html'