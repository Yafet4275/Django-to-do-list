from django.shortcuts import render, redirect
from .forms import AddTask

tasks = []

def home(request):
	context = {'tasks' : tasks}
	return render(request, "todo/home.html", context)

def add(request):
	if request.method == 'POST':
		form = AddTask(request.POST)
		if form.is_valid():
			task = form.cleaned_data["task"]
			tasks.append(task)
			return redirect('home')
		
	else: 
		form = AddTask()

	context = {'form' : form}
	return render(request, "todo/add.html", context)

