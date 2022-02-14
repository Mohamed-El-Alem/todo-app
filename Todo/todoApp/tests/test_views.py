from django.test import TestCase, Client
from django.urls import reverse
from todoApp.models import Todo
import json
class testViews(TestCase):
    def setUp(self):
            self.client = Client()
            self.todo_list_url = reverse('todo_list')
            self.todo_list_url = reverse('todo_add')


    def test_todo_list_GET(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list.html')

    def test_todo_add_GET(self):
        response = self.client.get(reverse('todo_add'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_todo.html')
            
    
    def test_todo_delete_GET(self):
        response = self.client.get(reverse('todo_delete'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_todo.html')
