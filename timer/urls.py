from django.urls import path 
from . import views

urlpatterns = [
	path("", views.list_timers, name="timer_list"), 
	path("timer/<int:pk>", views.detail_timer, name="timers_detail"),
    path("timer/create", views.create_timer, name="create_timer")
] 
