#coding:utf-8

from django.shortcuts import redirect
from django.http import  HttpResponseRedirect

def login(func):
    """"""
    def login_func(request, *args, **kwargs):
        """"""
        if request.session.has_key("user_id"):# cha zhao zhe ge zhi shi fou cun zai
            return func(request, *args, **kwargs)# yao shi zhe ge shi cun zai jiu jiang zhe ge zhi fan fang hui qu
        else:
            red = HttpResponseRedirect("/login/")# fu zhe jiu mei you deng long jiu fang hui dao deng long ye ming
            red.set_cookie("url", request.get_full_path())# ji long zhe shang ci fang wen de xin xi deng long zhi hou zhi jie hou dao zhe ge ye mian lai
            return red

    return login_func