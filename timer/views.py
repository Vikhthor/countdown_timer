from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import RegisterForm, CreateTimer
from .models import Timer

# Create your views here.

def list_timers(request):
    timers = []
    if request.user.is_authenticated:
        user = request.user.pk
        timers = Timer.objects.filter(owner=user)	
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
            return redirect('login') 
    else:
        form = RegisterForm()
    return render(request, "timer/register.html", {"form": form})

def create_timer(request):
    if request.method == "POST":
        req_data = request.POST.dict()
        req_data.update({'owner': request.user.pk})
        form = CreateTimer(req_data) 
        if form.is_valid() and request.user.is_authenticated:
            form.save()
            messages.success(request, "Timer created successfully!")
            return redirect('timer_list') 
    else:
        form = CreateTimer()
    return render(request, "timer/create.html", {"form": form})