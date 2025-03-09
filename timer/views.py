from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import RegisterForm, CreateTimer
from .models import Timer

# Create your views here.

def list_timers(request):	
    timers = Timer.objects.all()	
    return render(request, "timer/list.html", {"timers": timers}) 

def detail_timer(request, pk):	
    timer = get_object_or_404(Timer, pk=pk)	
    return render(request, "timer/detail.html", {"timer": timer}) 

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect('timer_list') 
    else:
        form = RegisterForm()
    return render(request, "timer/register.html", {"form": form})

def create_timer(request):
    if request.method == "POST":
        form = CreateTimer(request.POST) 
        if form.is_valid() and request.user.is_authenticated:
            form.owner = request.user
            form.save()
            messages.success(request, "Timer created successfully!")
            return redirect('timer_list') 
        else:
            form = CreateTimer()
    return render(request, "timer/create.html", {"form": form})