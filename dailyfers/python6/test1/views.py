#coding:utf-8

from django.shortcuts import render
from models import Inof, Books
# Create your views here.


def index(request):
    """"""
    user = Inof()
    user.title = "模仿游戏"
    user.date = "1990,2,5"

    contest = {"name":"茶壶", "list":user}
    return render(request, "booktest/index.html", contest)

def index_2(request):
    """"""
    pser = Books()
    pser.guanyu = "关羽"
    pser.zhafei = "张飞"
    pser.zilong = "子龙"
    pser.xuda = "熊大"
    pser.xuer = "熊二"
    contest = {"name":"你是我的神", "list":pser}
    return render(request, "booktest/index_2.html", contest)




