from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
import datetime
from .models import *
from .forms import *
# Create your views here.


#view tasks
@login_required
def home(request):
	template = 'home.html'
	form = addTaskForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Task Successfully Created")
		return redirect('/')
	queryset = tasks.objects.all()
	context = {
		"queryset":queryset,
		"form":form
	}
	return render( request, template, context)

#delete task
@login_required
def deleteTask(request, pk):
	template = 'delete_tasks.html'
	task = tasks.objects.get(id=pk)
	if request.method == 'POST':
		task.delete()
		messages.success(request, 'Successfully Deleted')
		return redirect('/')
	return render(request, template)



#update task
@login_required
def updateTask(request, pk):
	queryset = tasks.objects.get(id=pk)
	form = updateTaskForm(instance=queryset)
	templates =  "home.html"
	if request.method == 'POST':
		form = addTaskForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Task Successfully updated')
			return redirect('/')

	context = {
		'form':form
	}
	return render(request, templates, context)