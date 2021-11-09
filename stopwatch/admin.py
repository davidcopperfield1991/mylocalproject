from django.contrib import admin

# Register your models here.
from stopwatch.models import TimeDetail


class TimeDetailAdmin(admin.ModelAdmin):
    list_display = ['__str__', "title" , "total_time" ]


    class Meta:
        model = TimeDetail


admin.site.register(TimeDetail)