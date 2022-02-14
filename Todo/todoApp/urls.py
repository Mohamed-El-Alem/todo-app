
from django import views
from django.urls import path
from . views import TodoAddView
from .import views

urlpatterns = [
    path('', views.todoList, name="todo_list"),
    path('todo_add/', TodoAddView.as_view(), name="todo_add"),
    path('todo_delete/<todo_id>', views.todoDelete, name="todo_delete"),
    path('todo_complete/<todo_id>', views.todoComplete, name="todo_complete"),
    path('todo_uncomplete/<todo_id>', views.todoUncomplete, name="todo_uncomplete"),
    path('profile', views.profile, name="profile"),
    path('export_todo', views.todoExport, name="todo_export"),
    path('statistics', views.statistics, name="statistics"),
    path('import-csv', views.todoImport, name="todo_import"),

    

]
