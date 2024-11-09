from importlib.resources import contents

from django.http import HttpResponse
from django.shortcuts import render
from .models import TodolistItem
from django.http import HttpResponseRedirect

# Create your views here.

def todoappView(request):
    all_todo_items = TodolistItem.objects.all()
    return render(request, "todolist.html",
                  {"all_items":all_todo_items})


def addTodoView(reqest):
    x = reqest.POST['content']
    new_item = TodolistItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')
