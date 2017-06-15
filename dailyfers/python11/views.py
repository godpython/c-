#coding:utf-8
from django.shortcuts import render

# Create your views here.

def temp():
    """"""
    for item in range(1,11):
        if item:
            yield item
        yield "\n"

def run(request):
    """"""
    context = {"name":"", "list":temp()}
    return render(request, "booktest/run.html", context)