from django.shortcuts import render, redirect
from django.utils import timezone
from .models import ToDo

def toDo(request):
    obj_list = ToDo.objects.all().order_by("-added_date")
    return render(request, "index.html", {"obj_list" : obj_list})

def add_toDo(request):
    added_date = timezone.now()
    note = request.POST.get("note")
    if note == "":
        return redirect("ToDo")
    else:
        obj = ToDo(note=note, added_date=added_date)
        obj.save()
        return redirect("ToDo")


def del_toDo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return redirect("ToDo")