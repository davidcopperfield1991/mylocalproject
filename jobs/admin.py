from django.contrib import admin

# Register your models here.


from .models import Jobs, JobsTime , JobsCategory ,JobsTags


class jobsAdmin(admin.ModelAdmin):
    list_display = ['__str__', "title" , "active"]


    class Meta:
        model = Jobs , JobsTags



admin.site.register(Jobs , jobsAdmin)
admin.site.register(JobsTime)
admin.site.register(JobsCategory)
admin.site.register(JobsTags)
