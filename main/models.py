from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
user = get_user_model()


class ToDoList(models.Model):
    user = models.ForeignKey(user, default=1, related_name='todolist', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList,related_name='item', on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    completion = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.text
