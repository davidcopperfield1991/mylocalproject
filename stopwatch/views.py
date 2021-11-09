import json

from django.core import serializers
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
import decimal
# Create your views here.
import datetime

from jobs.models import Jobs, JobsCategory, JobsTags
from stopwatch.models import TimeDetail
import matplotlib.pyplot as plt,mpld3


def is_ajax(request):
    if (request.GET or None):
        p = request.GET.get('name')
        category = p
        data = Jobs.objects.filter(category__title=category)
        print(category)
        print("this is ajax signal")
        print(data)
        return data



def stopwatch(request):
    tags = JobsTags.objects.all()
    categorys = JobsCategory.objects.all()
    category = categorys.first()

    if (request.GET or None):
        # categorys = JobsCategory.objects.all()
        p = request.GET.get('name')
        category = p
        data = Jobs.objects.filter(category__title=category)
        print(category)
        print("this is ajax signal")
        data5 = serializers.serialize('json', data)
        print(data5)
        # pul = data.values_list('title')
        # pul2 = JsonResponse(data)
        return JsonResponse({'msg':'success' , 'pul': data5})


    data = Jobs.objects.filter(category__title=category)


    if (request.POST or None):
        category = request.POST.get("category")
        onwan = request.POST.get("onwan")
        tag = request.POST.get("tag")
        description = request.POST.get("description")
        start = request.POST.get("start")
        stop = request.POST.get("stop")
        total = request.POST.get("total")

        TimeDetail.objects.create(category=category,title=onwan,tag=tag,description=description,start_time=start,stop_time=stop,total_time=total)

    context = {
        'category': categorys,
        'data' : data,
        'tag' : tags
    }
    return render(request , "stopwatch.html" , context)


def chart(request):
    times = TimeDetail.objects.all()
    t = []
    i = []
    for annnn in times:
        times2 = (annnn.total_time)
        hhmmss = str(times2)
        [hours, minutes, seconds] = [int(x) for x in hhmmss.split(':')]
        x = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        nemidona = decimal.Decimal(x.seconds)
        vaghan_nemidunam = str(nemidona)
        i.append(int(vaghan_nemidunam))


    for ti in times:
        # print(ti)
        tss = ti.title
        # print(tss)
        t.append(tss)

    an = t
    mylist = json.dumps(an)
    # context = {'mylistjson': mylist}
    # print(i)
    # print(t)
    # an = serializers.serialize('json', t)
    # jj = JsonResponse.serialize(t)
    # print(jj)
    return render(request,"chart.html",{  'mylist' : mylist , 'zaman': i }  )








