from django import forms
from .models import Item, ToDoList


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name")


class CreateNewItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['todolist', 'text', 'completion']