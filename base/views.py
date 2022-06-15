from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Task
from django.urls import reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

#to redirect to some pageor some part of a page
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')



class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task

    #edit the template name from the default task_detail to task
    template_name = 'base/task.html'
 
#creating the list view as a class
class TaskList(LoginRequiredMixin,ListView):
   model = Task

   # to replace "object_list" with "tasks" in the template
   context_object_name = 'tasks'



class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    #the form is created by default by createview, we just have to set up the field
    #we could choose some items in the field : field= ['title', 'description']

    #if we wan list out all of the items inthefield we could just do as fellow:
    fields = '__all__'

    #we put the url name as an attribute, so it redirects to that url
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task 
    fields= '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task 
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')