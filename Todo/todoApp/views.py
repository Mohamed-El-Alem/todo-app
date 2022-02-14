
import io
from re import template
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Todo
from .forms import todoForm
import csv
from .mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url="login")
def todoList(request):
    todo_list = Todo.objects.all()  
    return render(request, 'todo_list.html' , {'todo_list':todo_list})

class TodoAddView(CreateView):
    model = Todo
    form_class=todoForm
    template_name='add_todo.html'

@login_required(login_url="login")
def statistics(request):
    completed=Todo.objects.filter(is_completed='Not_completed').count()
    uncompleted=Todo.objects.filter(is_completed='completed').count()
    return render(request, 'statistics.html', {'completed':completed, 'uncompleted':uncompleted})

@login_required(login_url="login")
def todoDelete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo_list')


@login_required(login_url="login")
def profile(request):
    todo_list = Todo.objects.all()  
    return render(request, 'profile.html' , {'todo_list':todo_list})

@login_required(login_url="login")
def todoComplete(request, todo_id): 
    item = Todo.objects.get(pk=todo_id)
    item.is_completed = 'completed'
    item.save() 
    return redirect('todo_list')


@login_required(login_url="login")
def todoUncomplete(request, todo_id): 
    item = Todo.objects.get(pk=todo_id)
    item.is_completed = 'Not completed'
    item.save() 
    return redirect('todo_list')

@login_required(login_url="login")
def todoExport(request):
    response = HttpResponse(content_type='text/csv')
    response ['Content-Disposition'] = 'attachment; filename.csv'
    # create a CSV writer
    writer = csv.writer(response)
    # design the model
    todos = Todo.objects.all()
    # add column heading to the CSV
    writer.writerow(['User', 'Todo', 'Status', 'Created', 'Updated'])
    # loop and output

    for todo in todos:
        writer.writerow([todo.user, todo.text, todo.is_completed, todo.created_time, todo.last_updated])

    return response

def todoImport(request):
    template="upload_csv.html"
    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'this is not a csv fiel')
    data_set =  csv_file.read().decode('UTF-8')
    io_string = io.StringIO (data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _,created = Todo.objects.update_or_create(
            user = column[0],
            text = column[1]
        )
    context = {}
    return render (request, template, context)
    
    






