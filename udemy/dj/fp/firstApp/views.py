from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert':"coming from firstApp/index"}
    return render(request, 'firstApp/index.html', context=my_dict)

    #return  HttpResponse("<h1>hello Haim</h1>")