import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todoApp.views import todoList, TodoAddView,todoDelete, profile, todoComplete, statistics, todoUncomplete, todoExport

class testUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('todo_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, todoList)

    def test_add_url_is_resolved(self):
        url = reverse('todo_add')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TodoAddView)

    def test_delete_url_is_resolved(self):
        url = reverse('todo_delete', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, todoDelete)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_statisctics_url_is_resolved(self):
        url = reverse('statistics')
        print(resolve(url))
        self.assertEquals(resolve(url).func, statistics)

    def test_complete_url_is_resolved(self):
        url = reverse('todo_complete', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, todoComplete)

    def test_uncomplete_url_is_resolved(self):
        url = reverse('todo_uncomplete', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, todoUncomplete)
    
    def test_export_url_is_resolved(self):
        url = reverse('todo_export')
        print(resolve(url))
        self.assertEquals(resolve(url).func, todoExport)
    
    
    

