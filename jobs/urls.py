"""mylocalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jobs.views import jobs_page, report, test, GetAllData, GetLocalData , UpdateData ,PostData , SearchData , DeleteData , all_api , today
from mylocalproject.views import home_page

urlpatterns = [
    path('jobspage', jobs_page),
    path('report', report),
    path('today', today,name="today"),
    path('all', test),
    path('getalldef', all_api),
    path('getall', GetAllData.as_view()),
    path('getlocal', GetLocalData.as_view()),
    path('getedit/<int:pk>', UpdateData.as_view()),
    path('postdata', PostData.as_view()),
    path('searchdata', SearchData.as_view()),
    path('deletedata/<int:pk>', DeleteData.as_view()),
    # path('startthat', start_that),

]
