#coding:utf-8

from django.shortcuts import render

# Create your views here.


def index(request):
    """"""
    contest = {"title":"你是我的神", "list":[1,2,34,5,6,7,8,9,10]}

    return render(request, "booktest/index.html", contest)