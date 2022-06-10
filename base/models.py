from msilib.schema import Class
from django.db import models

#import the user's tables built by default in django
from django.contrib.auth.models import User

# Create your models here.

#a class is like a db's table
class Task(models.Model):
    #cascade -> the elements of the user are deleted when the user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    #the title is a string
    title = models.CharField(max_length = 200)
    #textfield is a string with more options
    description = models.TextField(null= True, blank= True)
    complete = models.BooleanField(default= False)
    create = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
