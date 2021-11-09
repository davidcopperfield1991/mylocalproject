from django.shortcuts import render


def home_page(request):
    context = {
            'data' : 'new data'
    }

    return render(request,"homepage.html",context)



def main(request):
    context = {
            'data' : 'new data'
    }

    return render(request,"main.html",context)