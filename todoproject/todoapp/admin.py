from django.contrib import admin
from .forms import * 
# Register your models here.



class addTaskAdmin(admin.ModelAdmin):
	list_display = ['name', 'In_progress', 'dead_line', 'created', 'updated']
	form = addTaskForm
	list_filter = ['name', 'In_progress', 'dead_line']
	search_fields = ['name']

admin.site.register(tasks, addTaskAdmin)