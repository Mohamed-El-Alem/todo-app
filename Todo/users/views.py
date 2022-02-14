from re import template
from urllib.request import Request
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import *


def register_user(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, ("Account successfully created for "+ username))
            return redirect('login')
    context={'form':form}
    return render(request, 'authenticate/register.html', context)



# class UserRegisterView(generic.CreateView):

#     form_class = UserCreationForm
#     template_name= 'registration/register.html'
#     success_url  = reverse_lazy('login')

def login_user(request):
     if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             return redirect('todo_list')
    
         else:
             messages.success(request, ("there was an error, try again!"))
             return redirect('login')
     else:
          return render (request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('login')
