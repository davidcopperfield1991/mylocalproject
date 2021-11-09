from django.urls import path

from stopwatch.views import stopwatch, chart

urlpatterns = [
    path('stopwatch', stopwatch),
    path('chart', chart),

    # path('show', show),



]