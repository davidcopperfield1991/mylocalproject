from django.db import models
from datetime import date
# Create your models here.
from django.db.models import Q


class TimeDetailManager(models.Manager):


    def get_exact(self,name):
        lookup = (Q(title__icontains=name))
        return self.get_queryset().filter(lookup)

class TimeDetail(models.Model):

    category = models.CharField(max_length=200 ,null=True)
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=200 ,null=True)
    description = models.TextField(max_length=5000,null=True,blank=True)
    date = models.DateField(blank=True, default=date.today)
    start_time = models.TimeField(default="00:00:00" ,  blank=True)
    stop_time = models.TimeField(default="00:00:00" ,blank=True)
    total_time = models.TimeField(default="00:00:00", blank=True)

    def __str__(self):
        return self.title
    def total(self):
        return self.total_time


    class Meta:
        verbose_name_plural = "stopwatch"
        verbose_name = "stopwatch"