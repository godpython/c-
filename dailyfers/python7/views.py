#coding:utf-8
from django.shortcuts import render

# Create your views here.


def index(request):
    """"""
    contest = {"itcast":"你是我的神", "name":"子羽"}
    return render(request, "booktest/index.html", contest)

def index_2(request, id):
    """"""
    contest = {"name":"你是我的神", "id":id}
    return render(request, "booktest/index.html", contest)