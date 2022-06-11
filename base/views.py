from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Task

from django.views.generic.detail import DetailView
from .models import Task
# Create your views here.

class TaskDetail(DetailView):
    model = Task

    #edit the template name from the default task_detail to task
    template_name = 'base/task.html'
 
#creating the list view as a class
class TaskList(ListView):
   model = Task

   # to replace "object_list" with "tasks" in the template
   context_object_name = 'tasks'
