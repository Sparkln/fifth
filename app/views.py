from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.


def first(request):
    return HttpResponse('<h1><marquee>My life is worst without god....</marquee></h1>')
def second(request):
    return HttpResponse('<h1><marquee>Without laughter one day is like hell.....</marquee></h1>')
def third(request):
    return HttpResponse('<marquee><h1>I love my country❤️❤️❤️</h1></marquee>')
def fourth(request):
    return HttpResponse('<h1><marquee>Everyday is a new page of your life so write is by own</marquee></h1>' )