from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm


def index(request):
	todo_list = Todo.objects.order_by('id')
	form = TodoForm()

	context = {
		'todo_list': todo_list,
		'form': form,
	}

	return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
	form = TodoForm(request.POST)

	if form.is_valid():
		new_todo = Todo(text=form.cleaned_data['text'])
		new_todo.save()

	return redirect('index')


def completeTodo(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.complete = True
	todo.save()

	return redirect('index')


def deleteTodo(request, todo_id):
	Todo.objects.get(pk=todo_id).delete()
	return redirect('index')


def uncompleteTodo(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.complete = False
	todo.save()
	return redirect('index')


@require_POST
def editTodo(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.text = request.POST['text']
	todo.save()
	return redirect('index')


def deleteCompleted(request):
	Todo.objects.filter(complete__exact=True).delete()
	return redirect('index')


def deleteAll(request):
	Todo.objects.all().delete()
	return redirect('index')


@require_POST
def deleteSelected(request):
	ids = request.POST.getlist('selected')
	Todo.objects.filter(pk__in=ids).delete()
	return redirect('index')