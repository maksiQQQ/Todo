from django.shortcuts import redirect, render, HttpResponse
from .models import *

def homepage(request):
    return render(request, "index.html")

def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, 'meeting.html', {"tomeet_list": tomeet_list})

def habits(request):
    tohabits_list = ToHabits.objects.all()
    return render(request, 'habits.html', {"tohabits_list": tohabits_list})

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")
    
def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_tomeet(request):
    form = request.POST
    persone = form["tomeet_persone"]
    tomeet = ToMeet(persone=persone)
    tomeet.save()
    return redirect(meeting)

def add_habits(request):
    form = request.POST
    name = form["tohabits_name"]
    tohabits = ToHabits(name=name)
    tohabits.save()
    return redirect(habits)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)