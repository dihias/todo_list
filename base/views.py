from multiprocessing import context
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

   def get_context_data(self, **kwargs):
    context =super().get_context_data(**kwargs)
    context['tasks'] = context['tasks'].filter(user=self.request.user)
    context['count'] = context['tasks'].filter(complete=False).count()
    return context



class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    #the form is created by default by createview, we just have to set up the field
    #we could choose some items in the field : field= ['title', 'description']

    #if we wan list out all of the items inthefield we could just do as fellow:
    fields = ['title','description','complete']

    success_url= reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

    #we put the url name as an attribute, so it redirects to that url
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task 
    fields= ['title','description','complete']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task 
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')