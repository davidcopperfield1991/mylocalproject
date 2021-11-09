from django.db import models
from django.db.models import Q, CASCADE
from datetime import date
# Create your models here.


class JobsTags(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "tags"
        verbose_name = "tag"



class JobsCategory(models.Model):
    title = models.CharField(max_length=200)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "categories"
        verbose_name = "categorie"




class JobsManager(models.Manager):


    def get_exact(self,name):
        lookup = (Q(title__icontains=name))
        return self.get_queryset().filter(lookup)






class Jobs(models.Model):
    title = models.CharField(max_length=200 )
    category = models.ForeignKey(JobsCategory , blank=True, on_delete=models.CASCADE , null=True)
    time = models.TimeField(default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "jobs"
        verbose_name = "job"


    def timeget(self):
        b = self.time
        # print(b)



class JobsTime(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(blank=True, default=date.today)
    now1 = models.TimeField(default=0)
    now2 = models.TimeField(default=0)


    objects = JobsManager()

    class Meta:
        verbose_name_plural = "works"
        verbose_name = "work"

    def __str__(self):
        return self.title
