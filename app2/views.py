from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def repo(request):
    return HttpResponse('<h1><marquee>Hiii this side is surya......</marquee></h1>')
def demo(request):
    return HttpResponse('<h1><marquee>Hello World......</marquee></h1>')