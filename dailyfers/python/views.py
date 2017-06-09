#coding:utf-8

from django.shortcuts import render,redirect
from models import UserInfo
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect
from . import user_decorator
from models import *


# Create your views here.

def index(request):
    """shuo ying """
    contest = {"title":"用户登录","yonghe":"用户注册"}
    return render(request, "booktest/index.html")

def register(request):
    """yong he zhu cheng """
    contest = {"title":"用户注册"}
    return render(request, "booktest/register.html", contest)

def register_handle(request):
    """yong hu de mi ma yang zheng """
    post = request.POST
    user_name = post.get("user_name")
    upwd = post.get("pwd")
    ucpwd = post.get("cpwd")
    uemail = post.get("email")
    if upwd != ucpwd:
        return redirect("/register/")# yong hu de mi ma bu yi zheng jiao yong hu chung xing kai shi zhu che

    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()

    user = UserInfo()
    user.uanme = user_name
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect("/login/")

def register_exist(request):
    """yong hu ming de yang cheng"""
    uname = request.GET.get("uname")
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({"count":count})

def login(request):
    """yong hu ding lu ye mian"""
    uname = request.COOKIES.get("uname", " ")
    contest = {"title":"用户登录", "error_name":0, "error_pwd":0, "uname":uname}
    return render(request, "booktest/login.html", contest)

# def login_handle(request):
#     """"""
#     post = request.POST
#     uname = post.get("username")
#     upwd = post.get("pwd")
#     jizhu = post.get("jizhu", 0)
#     users = UserInfo.objects.filter(uname=uname)# mei you du qu dao jiu fang hui yi ge kon de lie biao
#
#     if len(users) == 1:
#         s1 = sha1()
#         s1.update(upwd)
#         if s1.hexdigest() == users[0].upwd:
#             url = request.COOKIES.get("url", "/index/")
#             red = HttpResponseRedirect(url)
#
#             red.set_cookie("url", "", max_age= -1)
#
#             if jizhu != 0:
#                 red.set_cookie("uname", uname)
#             else:
#                 red.set_cookie("uname", "", max_age= -1)
#
#             request.session["user_id"] = users[0].id
#             request.session["user_name"] = uname
#             return red
#         else:
#             context = {"title":"用户登录", "error_name":0, "error_pwd":1, "uname":uname, "upwd":upwd}
#             return render(request, "booktest/login.html", context)
#     else:
#         context = {"title":"用户登录", "error_name":1, "error_pwd":0, "uname":uname, "upwd":upwd}
#         return render(request, "booktest/login.html", context)

def login_handle(request):
    """"""
    contest = {"title":"-ni-shi-wo-de-sheng", "yonghe":"退出"}
    return render(request, "booktest/index.html", contest)


def user_center_info(request):
    """"""
    user = UserInfo.objects.all()
    post = request.POST
    user.ushou = post.get("ushou", "-ni-shi-wo-de-sheng")
    user.uaddress = post.get("uaddress", "")
    user.uyoubian = post.get("uyoubian", "天堂")
    user.uphone = post.get("uphone", "123456789")
    contest = {"title":"用户中心","titl": "-ni-shi-wo-de-sheng", "yonghe": "退出", "user":user}
    return render(request, "booktest/user_center_info.html", contest)

def user_center_site(request):
    """"""
    user = UserInfo.objects.all()
    post = request.POST
    user.ushou = post.get("ushou", "")
    user.uaddress = post.get("uaddress", "")
    user.uyoubian = post.get("uyoubian", "")
    user.uphone = post.get("uphone", "")
    contest = {"title":"收货地址", "titl":"-ni-shi-wo-de-sheng", "yonghe": "退出","user":user}
    return render(request, "booktest/user_center_site.html", contest)

def detail(request):
    """"""
    contest = {"title":"最近浏览","titl":"-ni-shi-wo-de-sheng", "youghe":"退出"}
    return render(request, "booktest/detail.html",contest)

def list(request):
    """"""
    contest = {"title":"列表页","titl":"-ni-shi-wo-de-sheng", "youghe":"退出"}
    return render(request, "booktest/list.html", contest)

def qubu(request):
    """"""
    return render(request, "booktest/qubu.html")

def user_center_order(request):
    """"""
    contest = {"title":"全部商品", "titl":"-ni-shi-wo-de-sheng", "youghe":"退出"}
    return render(request, "booktest/user_center_order.html", contest)
#
# @user_decorator.login
# def user_center_info(request, pindex):
#     """"""
#     user_email = UserInfo.objects.get(id=request.session["user_id"]).uemail
#     goods_list = []
#     goods_ids = request.COOKIES.get("goods_ids", "")
#     if goods_ids != "":
#         goods_ids1 = goods_ids.split(",")
#         for goods_id in goods_ids1:
#             goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
#
#     contest = {"title":'用户中心',
#                "user_email":user_email,
#                "user_name":request.session["user_name"],
#                "page_name":1,
#                "goods_list":goods_list
#                }
#
#     return render(request, "booktest/user_center_info.html", contest)
#
# @user_decorator.login#
# def user_center_order(request,pindex):
#     order_list=OrderInfo.objects.filter(user_id=request.session['user_id']).order_by('-oid')
#     paginator=Paginator(order_list,2)
#     if pindex=='':
#         pindex='1'
#     page=paginator.page(int(pindex))
#
#     context={'title':'用户中心',
#              'page_name':1,
#              'paginator':paginator,
#              'page':page,}
#     return render(request,'booktest/user_center_order.html',context)


# @user_decorator.login
# def user_center_site(request, pindex):
#     """"""
#     user = UserInfo.objects.get(id=request.session["user_id"])
#     if request.method == "POST":
#         post = request.POST
#         user.ushou = post.get("ushou")
#         user.uaddress = post.get("uaddress")
#         user.uyoubian = post.get("uyoubian")
#         user.uphone = post.get("uphone")
#         user.save()
#
#     contest = {"title":"用户中心",
#                "user":user,
#                "page_name":1
#                }
#
#     return render(request, "booktest/user_center_site.html", contest)

def cart(request):
    """"""
    contest = {"title": "你的车", "titl": "-ni-shi-wo-de-sheng", "youghe": "退出"}
    return render(request, "booktest/cart.html", contest)


def place(request):
    """"""
    contest = {"title": "你的车", "titl": "-ni-shi-wo-de-sheng", "youghe": "退出"}
    return render(request, "booktest/place_order.html", contest)

def index_2(request):
    """"""
    contest = {"title":"ha ha"}
    return render(request, "booktest/index_2.html", contest)



