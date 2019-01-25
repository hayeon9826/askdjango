from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mysum(request, numbers):
    #request : HTTPREQUEST
    #numbers = '1/2/12/123/1232/1232/3213/1232'
    result = sum(map(int, numbers.split('/')))
    return HttpResponse(result)