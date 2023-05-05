from django import forms 
from .models import tasks
from django.utils.safestring import mark_safe

from django import forms

#add task
class addTaskForm(forms.ModelForm):
  class Meta:
    model = tasks
    fields = ['name', 'In_progress', 'dead_line']

#update task
class updateTaskForm(forms.ModelForm):
  class Meta:
    model = tasks
    fields = ['name', 'In_progress', 'dead_line']

