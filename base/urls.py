from django.urls import path

from .views import  TaskList, TaskCreate,TaskDetail, TaskUpdate, TaskDelete, CustomLoginView
from django.contrib.auth.views import LogoutView 

urlpatterns = [

path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),

path('login/', CustomLoginView.as_view(), name='login'),

path('task/<int:pk>/',TaskDetail.as_view(),name = "task"),

path('task-update/<int:pk>/',TaskUpdate.as_view(),name = "task-update"),

path('task-delete/<int:pk>/',TaskDelete.as_view(),name = "task-delete"),



#adding the url of the simple funtional view 
#we put an umpty string for the first argument so this url will be our base url
#for the 2nd argument we can't use a class directly, so we calla function inside the class 
#the 3rd argument is the name of the view in the url 'url pattern'
path('',TaskList.as_view(), name="tasks"),
path('task-create',TaskCreate.as_view(), name="task-create"),
]