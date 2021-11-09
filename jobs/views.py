import pandas as pd
import datetime

from django.shortcuts import render

# Create your views here.
from django.utils.timezone import now

from jobs.models import Jobs, JobsTime

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from jobs.serializers import HowRead
from rest_framework.decorators import api_view



class GetAllData(APIView):
    def get(self , request):
        query = JobsTime.objects.all()
        serializers = HowRead(query , many=True , context={'request' : request})
        return Response(serializers.data , status=status.HTTP_200_OK)

# context use for image url set

@api_view(['GET'])
def all_api(request):
    if request.method == 'GET':
        query = JobsTime.objects.all()
        serializer = HowRead(query , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)




class GetLocalData(APIView):
    def get(self , request):
        query = JobsTime.objects.filter(title='local')
        serializers = HowRead(query , many=True)
        return Response(serializers.data , status=status.HTTP_200_OK)


class UpdateData(APIView):
    def get(self,request,pk):
        query = JobsTime.objects.get(pk=pk)
        serializers = HowRead(query)
        return Response(serializers.data , status=status.HTTP_200_OK)


    def put(self,request,pk):
        query = JobsTime.objects.get(pk=pk)
        serializers = HowRead(query, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=status.HTTP_201_CREATED)
        return Response(serializers.errors , status=status.HTTP_400_BAD_REQUEST)


class PostData(APIView):
    def post(self,request):
        serializers = HowRead( data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=status.HTTP_201_CREATED)
        return Response(serializers.errors , status=status.HTTP_400_BAD_REQUEST)


class SearchData(APIView):
    def get(self , request):
        search = request.GET['name']
        query = JobsTime.objects.filter(title__contains=search)
        serializers = HowRead(query , many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)


class DeleteData(APIView):
    def delete(self,request,pk):
        query = JobsTime.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def jobs_page(request):

    data = Jobs.objects.all()

    if request.GET != None:
        sawoj = request.GET.get("sd")
        if request.POST != None:
            sawojj = request.POST.get("bapost")
            sawojbolagh = request.POST.get("bapost")
            sawojbolagh2 = request.POST.get("bapost2")
        sawojbolagh = sawojbolagh2
        print(sawojbolagh)


    # job_title = list(request.GET)
    # print(job_title)


    def get_time(type):


        if type == "start":
            now1 = datetime.datetime.now()
            JobsTime.objects.create(title=sawojbolagh,now2="00:00:00" , now1=now1 )
        elif type == "stop":
            now2 = datetime.datetime.now()
            print(now2)
            qs = JobsTime.objects.all().filter(title=sawojbolagh).last()
            qsid = qs.id
            JobsTime.objects.filter(id=qsid).update(now2=now2)




    if (request.POST or None):
        keys=list(request.POST.keys())
        print(keys)
        type = (keys[2])
        if type == "start":
            get_time(type=
                     "start")


        elif type == "stop":
            get_time(type="stop")

        else:
            print("sawoj")

    context = {
        'test': data
    }




    return render(request,"jobspage.html",context)





# def report(request):
#     data = Jobs.objects.all()
#     if request.GET != None:
#         sawoj = request.GET.get("sd")
#         sawojbolagh = request.GET.get("sp")
#     gozaresh = list(JobsTime.objects.filter(title=sawojbolagh).values('now1', 'now2'))
#     l = 0
#
#     def time():
#         return now()
#
#     time = time()
#     for i in gozaresh:
#
#         now1 = gozaresh[l].get('now1').replace(microsecond=0)
#         now2 = gozaresh[l].get('now2').replace(microsecond=0)
#
#         t1 = datetime.datetime.strptime(str(now1), "%H:%M:%S")
#         t2 = datetime.datetime.strptime(str(now2), "%H:%M:%S")
#         print(t2 - t1)
#         time += t2 - t1
#         l += 1
#
#     print ((time-now()))
#     print(time)
#     ersali = time.replace(microsecond=0) -now().replace(microsecond=0)
#
#     context = {
#         'object': ersali,
#         'test': data
#
#     }
#     return render(request, "report.html", context)
#

def test(request):
    data = Jobs.objects.all()
    #
    # if (request.POST or None):
    #     keys=list(request.POST.keys())
    #     # print(keys)
    #     type = (keys[1])
    #     if type == "bapost2":
    #         sawojbolagh2 = request.POST.get("bapost2")
    #         sawojbolagh = sawojbolagh2

    if request.POST != None:
        keys = list(request.POST.keys())
        print(keys)
        if len(keys) > 0:
            type = (keys[1])
            print(type)
            if type == 'bapost2':
                print('salam')

        sawojbolagh2 = request.POST.get("bapost2")
        sawojbolagh = sawojbolagh2
    print(sawojbolagh)


    gozaresh = list(JobsTime.objects.filter(title=sawojbolagh2).values('now1', 'now2'))
    l = 0

    # if request.POST != None:
        # sawoj = request.GET.get("sd")
        # sawojbolagh = request.GET.get("sp")
    gozaresh = list(JobsTime.objects.filter(title=sawojbolagh).values('now1', 'now2'))
    l = 0
    # print(gozaresh)



    def time():
        return now()

    time = time()
    for i in gozaresh:

        now1 = gozaresh[l].get('now1').replace(microsecond=0)
        now2 = gozaresh[l].get('now2').replace(microsecond=0)

        t1 = datetime.datetime.strptime(str(now1), "%H:%M:%S")
        t2 = datetime.datetime.strptime(str(now2), "%H:%M:%S")
        # print(t2 - t1)
        time += t2 - t1
        l += 1


    # print ((time-now()))
    print(time)
    ersali = time.replace(microsecond=0) -now().replace(microsecond=0)
    print(ersali)




    # baraye seri start o stop :


    def get_time(type):
        print(type)


        if type == "start":
            now1 = datetime.datetime.now()
            JobsTime.objects.create(title=sawojbolagh,now2=now1 , now1=now1 )
        elif type == "stop":
            now2 = datetime.datetime.now()
            print(now2)
            qs = JobsTime.objects.all().filter(title=sawojbolagh).last()
            qsid = qs.id
            JobsTime.objects.filter(id=qsid).update(now2=now2)




    if (request.POST or None):
        keys=list(request.POST.keys())
        print(keys)
        type = (keys[2])
        if type == "start":
            get_time(type="start")


        elif type == "stop":
            get_time(type="stop")

        else:
            print("sawoj")

    context = {
        'object': ersali,
        'test': data,
        'ann' : sawojbolagh2

    }
    return render(request, "all.html", context)


# def report(request):
#     data = JobsTime.objects.all().values()
#     j = pd.DataFrame()
#     dataa = list(data)
#     j = j.append(dataa)
#     j['rrr'] = str(j['now1'])
#
#     # k = j[j.title == 'local']
#     # print(k)
#
#     # j.to_csv('sttsdht')
#     print(j)

def report(request):
    data = Jobs.objects.all()
    timesh = JobsTime.objects.all().values()
    j = pd.DataFrame()
    data2 = list(timesh)
    j = j.append(data2)
    print(j['date'].nunique())
    lll = j['date']
    p = str(lll)
    p = p.replace("datetime.date", "")
    # p = p.re
    lll = list(lll.unique())
    # lll = lll.re
    print(p)




    if request.GET != None:
        sawoj = request.GET.get("sd")
        sawojbolagh = request.GET.get("sp")
    gozaresh = list(JobsTime.objects.filter(title=sawojbolagh ).values('now1', 'now2'))
    l = 0

    def time():
        return now()

    time = time()
    for i in gozaresh:

        now1 = gozaresh[l].get('now1').replace(microsecond=0)
        now2 = gozaresh[l].get('now2').replace(microsecond=0)

        t1 = datetime.datetime.strptime(str(now1), "%H:%M:%S")
        t2 = datetime.datetime.strptime(str(now2), "%H:%M:%S")
        print(t2 - t1)
        time += t2 - t1
        l += 1

    print ((time-now()))
    print(time)
    ersali = time.replace(microsecond=0) -now().replace(microsecond=0)

    context = {
        'object': ersali,
        'test': data,
        'time': p

    }
    return render(request, "report.html", context)





def today(request):
    data = Jobs.objects.all()
    whatsday = datetime.datetime.today()

    print(whatsday)


    if request.GET != None:
        gozaresh = list(JobsTime.objects.filter(date=whatsday).values('now1', 'now2'))
    l = 0

    def time():
        return now()

    time = time()
    for i in gozaresh:

        now1 = gozaresh[l].get('now1').replace(microsecond=0)
        now2 = gozaresh[l].get('now2').replace(microsecond=0)

        t1 = datetime.datetime.strptime(str(now1), "%H:%M:%S")
        t2 = datetime.datetime.strptime(str(now2), "%H:%M:%S")
        print(t2 - t1)
        time += t2 - t1
        l += 1

    print ((time-now()))
    print(time)
    ersali = time.replace(microsecond=0) -now().replace(microsecond=0)


    context = {
        'object': ersali,
        'test': data,


    }
    return render(request, "today.html", context)