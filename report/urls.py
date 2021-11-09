from django.urls import path

from report.views import chartlib , test ,mainchart , detail , secondchart

urlpatterns = [

    path('chartlib', chartlib),
    path('test', test),
    path('mainchart', mainchart,name='mainchart'),
    path('secondchart', secondchart,name='secondchart'),
    path('detail', detail),

]