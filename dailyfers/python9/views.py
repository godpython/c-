#coding:utf-8

from django.shortcuts import render

# Create your views here.

def data(request):
    """"""
    contest = {"name":"子羽", "list":[1,2,3,4,5,6,7,8,9,10]}
    return render(request, "booktest/data.html", contest)

def date(request):
    """"""
    contest = {"name":"大剑士", "queue":"假如爱是有限生命的沉淀那么我对你爱会被无限的时间冲淡吗"}
    return render(request, "booktest/date.html", contest)