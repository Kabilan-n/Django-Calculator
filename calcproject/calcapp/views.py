from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def index(request):
    return render(request,'index.html')

def submitquery(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        mydictionary = {
            "Q" : q,
            "ans" : ans,
            "error" : False,
            "result" : True

        }
        return render(request,'index.html',context = mydictionary)

    except:
        mydictionary = {
            "Q" : q,
            "error" : True,
            "result" : True
        }
        return render(request,'index.html',context = mydictionary)
    