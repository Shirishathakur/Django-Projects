from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse("Hello World")

def say_hello_html(request):
    return render(request,"hello.html")


def say_hello_html_Siri(request):
    return render(request,"helloSiri.html",{"name":"Siri"})

def say_hello_html_conditional(request):
    return render(request,"helloSiriConditional.html",{"name":"Mani"})


