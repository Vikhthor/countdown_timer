from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.urls import reverse

# Create your models here.

timer_min_validator = MinValueValidator(limit_value=0, message="Minimum timer value is 0") 
minutes_max_validator = MaxValueValidator(limit_value=59, message="Maximum minutes value is 59") 
seconds_max_validator = MinValueValidator(limit_value=59, message="Maximum seconds value is 59") 

class Timer(models.Model): 
    title = models.CharField(max_length=250, default='No title')
    hours = models.IntegerField(default=0, validators=[timer_min_validator]) 
    minutes = models.IntegerField(default=0, validators=[timer_min_validator, minutes_max_validator]) 
    seconds = models.IntegerField(default=0, validators=[timer_min_validator, seconds_max_validator]) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return self.title 

    def get_absolute_url(self):
        return reverse("timer_detail", kwargs={'pk': self.pk}) 
