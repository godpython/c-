#coding:utf-8
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def index_10(request):
    """"""
    contest = {"name":"你是我的神", "list":[1,2,3,4,5,6,7,8,9,10]}
    return render(request, "booktest/test.html", contest)

def test2(request):
    """"""
    contest = {"name":"爱是永恒的信念"}
    return redirect("/user/index_10/", contest)