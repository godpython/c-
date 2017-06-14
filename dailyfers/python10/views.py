#coding:utf-8
from django.shortcuts import render

# Create your views here.

def python(request):
    """"""
    contest = {"name":"你是我的神", "list":[i for i in range(1,20)]}
    return render(request, "booktest/python.html", contest)