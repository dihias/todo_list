from django.urls import path

#import my views , . because they are in the same file structure 
from .views import TaskDetail

urlpatterns = [

path('task/<int:pk>/',TaskDetail.as_view(),name = "task")
]