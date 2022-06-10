from django.urls import path

#import my views , . because they are in the same file structure 
from . import views

urlpatterns = [
#adding the url of the simple funtional view 
#we put an umpty string for the first argument so this url will be our base url
#for the 2nd argument we havethe file "views" dot the name of the function of the view "tasklist"
#the 3rd argument is the name of the view in the url 'url pattern'
path('',views.tasklist, name="tasks"),
]