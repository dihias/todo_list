from django.contrib import admin

#import the model that we created
from .models import Task

#register the model that we created with the admin panel (to see it in the admin panel)
admin.site.register(Task)
