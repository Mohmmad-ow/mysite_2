from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList, CreateNewItem

# Create your views here.


def index(request):
    tl = ToDoList.objects.all()
    return render(request, 'main/index.html', {'ToDoList': tl})


def to_so_lists(response, id):
    ls = ToDoList.objects.get(id=id)
    it = ls.item.all()
    if response.method == "POST":

        if response.POST.get('SaveAll'):

            text = response.POST.get('new')
            if len(text) > 3:
                new_item = ls.item.create(text=text, completion=False)
                new_item.save()
            for item in it:
                if response.POST.get('c' + str(item.id)) == 'clicked':
                    item.completion = True
                else:
                    item.completion = False
                item.save()
        elif response.POST.get('save'):
            for item in it:
                if response.POST.get('c' + str(item.id)) == 'clicked':
                    item.completion = True

                else:
                    item.completion = False
                item.save()

        elif response.POST.get('NewItem'):
            text = response.POST.get('new')
            if len(text) > 3:
                new_item = ls.item.create(text=text, completion=False)
                new_item.save()
        elif response.POST.get('delete'):
            tl = ToDoList.objects.get(id=id)
            tl.delete()
            return redirect('/')
        for item in it:
            if response.POST.get('d' + str(item.id)) == 'delete_item':
                item.delete()
                return redirect('/')
    return render(response, 'main/view.html', {'to_do_list': ls, 'items': it})


def create_form(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST or None)
        if form.is_valid():
            n = form.cleaned_data['name']
            request.user.todolist.create(name=n)

    else:
        form = CreateNewList()

    return render(request, 'main/create.html', {'form': form})


def user_tdl(request):
    return render(request, 'main/user_lists.html',{})