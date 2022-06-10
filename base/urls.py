from django.urls import path

#import my view tasklist this way because it's a class 
from .views import TaskList

urlpatterns = [
#adding the url of the simple funtional view 
#we put an umpty string for the first argument so this url will be our base url
#for the 2nd argument we can't use a class directly, so we calla function inside the class 
#the 3rd argument is the name of the view in the url 'url pattern'
    path('',TaskList.as_view(), name="tasks"),
]