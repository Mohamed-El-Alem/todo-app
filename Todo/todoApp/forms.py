import imp
from tkinter import Widget
from django import forms 
from .models import Todo

class todoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["text", "user"]

        Widgets = {
             'text' : forms.TextInput(attrs={'class':'form-control'}),
             'user' : forms.Select(attrs={'class':'form-control'})
         }