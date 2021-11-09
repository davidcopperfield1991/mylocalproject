import datetime
import decimal
import json
import pandas as pd
from random import *
from django.shortcuts import render
import pymysql.cursors
import math
from bson import json_util
# Create your views here.

from django.utils.timezone import now

from jobs.models import Jobs, JobsTime
from stopwatch.models import TimeDetail


def chartsik(request):
    data = TimeDetail.objects.all()
    # print(data)
    t = []
    i = []
    for annnn in data:
        times2 = (annnn.total_time)
        hhmmss = str(times2)
        [hours, minutes, seconds] = [int(x) for x in hhmmss.split(':')]
        x = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        nemidona = decimal.Decimal(x.seconds)
        vaghan_nemidunam = str(nemidona)
        i.append(int(vaghan_nemidunam))


    for ti in data:
        tss = ti.title
        t.append(tss)
    print(i)

    an = t
    mylist = json.dumps(an)
    print(mylist)

    return render(request,"chart.html",{  'mylist' : mylist , 'zaman': i })

def chartgostar(titlee,timee,datee):
    data = TimeDetail.objects.all()
    # print(data)
    t = []
    for ti in data:
        tss = ti.title
        t.append(tss)

    an = t
    mylist = json.dumps(an)

    timesh = TimeDetail.objects.all().values()
    j = pd.DataFrame()
    data2 = list(timesh)
    j = j.append(data2)
    sik = pd.DataFrame()
    # sik['onwan'] = j['title']
    # sik['time'] = j['total_time']
    sik['onwan'] = j[str(titlee)]
    sik['time'] = j[str(timee)]
    sik['datetime'] = j[str(datee)]
    sik['Date'] = pd.to_datetime(sik['time'], format='%H:%M:%S')
    sik['allsecond'] = ((sik['Date'].dt.hour) * 3600) + (sik['Date'].dt.minute * 60) + (sik['Date'].dt.second)
    nahayat = pd.DataFrame()
    nahayat['onwan'] = sik['onwan']
    nahayat['time'] = sik['allsecond']
    df = pd.DataFrame(nahayat)
    sawoj = df.groupby(["onwan"]).sum().reset_index()
    nahayat2 = pd.DataFrame()
    nahayat2['time'] = sik['allsecond']
    nahayat2['date'] = sik['datetime']
    df2 = pd.DataFrame(nahayat2)
    sawojbolagh = df2.groupby(['date']).sum().reset_index()
    k = []
    k = list(sawoj['onwan'])
    i = []
    i = list(sawoj['time'])
    i = list(sawoj['time'])
    print(i)
    kee = i.reverse()
    # print(kee)
    nn = []
    sn = list(sawojbolagh['date'])
    rgba = []
    rgba = []
    for o in k:
        rgba.append(f"rgba({[randint(1, 255)][0]}, {[randint(1, 255)][0]} , {[randint(1, 255)][0]}, .85 )")
    for u in sn:
        nn.append(str(u))
    # print(k)
    # print(i)
    return k , i , nn,rgba


def chartlib(request):
    ll = chartgostar(titlee="title",timee="total_time",datee="date")
    # print(ll)
    k = ll[0]
    i = ll[1]
    nn = ll[2]
    rgba = ll[3]
    print(k)
    print(i)
    print(nn)
    print(rgba)






    return render(request,"chart.html",{  'mylist' : k , 'zaman': i })


def test(request):
    timesh = JobsTime.objects.all().values()
    j = pd.DataFrame()
    data2 = list(timesh)
    j = j.append(data2)
    sik = pd.DataFrame()
    sik['onwan'] = j['title']
    sik['time1'] = j['now1']
    sik['time2'] = j['now2']
    sik['Date1'] = pd.to_datetime(sik['time1'], format='%H:%M:%S.%f')
    sik['Date2'] = pd.to_datetime(sik['time2'], format='%H:%M:%S.%f')
    sik['allsecond1'] = ((sik['Date1'].dt.hour) *3600) + (sik['Date1'].dt.minute * 60) + (sik['Date1'].dt.second)
    sik['allsecond2'] = ((sik['Date2'].dt.hour) *3600) + (sik['Date2'].dt.minute * 60) + (sik['Date2'].dt.second)
    sik['total'] = sik['allsecond2'] - sik['allsecond1']
    nahayat = pd.DataFrame()
    nahayat['onwan'] = sik['onwan']
    nahayat['time'] = sik['total']
    # print(nahayat)
    df = pd.DataFrame(nahayat)
    # print(df.groupby(["onwan"]).sum())
    sawoj = df.groupby(["onwan"]).sum().reset_index()
    # print(sawoj)
    k = []
    k = list(sawoj['onwan'])
    print(k)
    jj = []
    jj = list(sawoj['time'])
    print(jj)




    return render(request,'test.html')


def miltohour(i):
    time = str(datetime.timedelta(seconds=i))
    return time



def mainchart(request):

    timesh = JobsTime.objects.all().values()
    j = pd.DataFrame()
    data2 = list(timesh)
    j = j.append(data2)
    sik = pd.DataFrame()
    sik['onwan'] = j['title']
    sik['tarikh'] = j['date']
    sik['time1'] = j['now1']
    sik['time2'] = j['now2']
    sik['Date1'] = pd.to_datetime(sik['time1'], format='%H:%M:%S.%f')
    sik['Date2'] = pd.to_datetime(sik['time2'], format='%H:%M:%S.%f')
    sik['allsecond1'] = ((sik['Date1'].dt.hour) * 3600) + (sik['Date1'].dt.minute * 60) + (sik['Date1'].dt.second)
    sik['allsecond2'] = ((sik['Date2'].dt.hour) * 3600) + (sik['Date2'].dt.minute * 60) + (sik['Date2'].dt.second)
    sik['total'] = sik['allsecond2'] - sik['allsecond1']
    nahayat = pd.DataFrame()
    nahayat['onwan'] = sik['onwan']
    nahayat['time'] = sik['total']
    df = pd.DataFrame(nahayat)
    sawoj = df.groupby(["onwan"]).sum().reset_index()
    nahayat2 = pd.DataFrame()
    nahayat2['tarikh'] = sik['tarikh']
    nahayat2['time'] = sik['total']
    df2 = pd.DataFrame(nahayat2)
    sawojbolagh = df2.groupby(["tarikh"]).sum().reset_index()
    # print(sawojbolagh)
    k = []
    k = list(sawoj['onwan'])
    jj = []
    i = list(sawoj['time'])
    ll = []
    ll = list(sawojbolagh['tarikh'])
    lc = list(sawojbolagh['time'])
    su = []
    for q in ll:
        su.append(str(q))
    rgba = []
    for o in k:
        rgba.append(f"rgba({[randint(1,255)][0]}, {[randint(1,255)][0]} , {[randint(1,255)][0]}, .85 )")
    print(lc)
    l = lc
    new = []
    s = 0
    for j in l:
        sawoj = miltohour(l[s])
        sawojbolagh = sawoj.replace(":","")
        new.append(sawojbolagh)
        s += 1
    print(new)
    return render(request, "mainchart.html", {'mylist': k, 'zaman': i , 'tarikh' : su , 'zuman' : new , 'rgba':rgba})


from IPython.display import HTML
def detail(request):
    data = JobsTime.objects.all().values()
    j = pd.DataFrame()
    data2 = list(data)
    j = j.append(data2)
    j = j.tail(10)
    result = j.to_html()
    print(result)
    # b = HTML(j.to_html(classes='table table-striped'))
    # print(b)
    context = {'result' : result}
    return render(request , 'detail.html' ,context=context)


def secondchart(request):

    timesh = JobsTime.objects.all().values()
    j = pd.DataFrame()
    data2 = list(timesh)
    j = j.append(data2)
    sik = pd.DataFrame()
    sik['onwan'] = j['title']
    sik['tarikh'] = j['date']
    sik['time1'] = j['now1']
    sik['time2'] = j['now2']
    sik['Date1'] = pd.to_datetime(sik['time1'], format='%H:%M:%S.%f')
    sik['Date2'] = pd.to_datetime(sik['time2'], format='%H:%M:%S.%f')
    sik['allsecond1'] = ((sik['Date1'].dt.hour) * 3600) + (sik['Date1'].dt.minute * 60) + (sik['Date1'].dt.second)
    sik['allsecond2'] = ((sik['Date2'].dt.hour) * 3600) + (sik['Date2'].dt.minute * 60) + (sik['Date2'].dt.second)
    sik['total'] = sik['allsecond2'] - sik['allsecond1']
    nahayat = pd.DataFrame()
    nahayat['onwan'] = sik['onwan']
    nahayat['time'] = sik['total']
    df = pd.DataFrame(nahayat)
    sawoj = df.groupby(["onwan"]).sum().reset_index()
    nahayat2 = pd.DataFrame()
    nahayat2['tarikh'] = sik['tarikh']
    nahayat2['time'] = sik['total']
    df2 = pd.DataFrame(nahayat2)
    sawojbolagh = df2.groupby(["tarikh"]).sum().reset_index()
    # print(sawojbolagh)
    k = []
    k = list(sawoj['onwan'])
    jj = []
    i = list(sawoj['time'])
    ll = []
    ll = list(sawojbolagh['tarikh'])
    lc = list(sawojbolagh['time'])
    su = []
    for q in ll:
        su.append(str(q))
    rgba = []
    for o in k:
        rgba.append(f"rgba({[randint(1,255)][0]}, {[randint(1,255)][0]} , {[randint(1,255)][0]}, .85 )")
    print(lc)
    l = lc
    new = []
    s = 0
    for j in l:
        sawoj = miltohour(l[s])
        sawojbolagh = sawoj.replace(":","")
        new.append(sawojbolagh)
        s += 1
    print(new)
    return render(request, "secondchart.html", {'mylist': k, 'zaman': i , 'tarikh' : su , 'zuman' : new , 'rgba':rgba})